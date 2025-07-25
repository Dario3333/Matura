import random
import csv

def dice_roll():
    return random.randint(1, 6) + random.randint(1, 6)

def auswertung(balance, passline, dpassline, come_results, passbet, dpassbet):
    if passline == "win":
        balance += 2 * passbet
    if dpassline == "win":
        balance += 2 * dpassbet
    if dpassline == "push":
        balance += dpassbet

    for result, bet in come_results:
        if result == "win":
            balance += 2 * bet
        elif result == "tie":
            balance += bet
    return balance

def game(balance, passbet, dpassbet, initial_come_bet):
    passline = ""
    dpassline = ""
    come_results = []
    total_come_bets = initial_come_bet

    sum = dice_roll()
    
    if sum == 7 or sum == 11:
        passline = "win"
        dpassline = "lose"
    elif sum == 2 or sum == 3:
        passline = "lose"
        dpassline = "win"
    elif sum == 12:
        passline = "lose"
        dpassline = "push"
    else:
        point = sum
        active_come_bets = {}
        # erste Come-Wette platzieren
        if initial_come_bet > 0:
            balance -= initial_come_bet
            come_roll = dice_roll()
            if come_roll in (7, 11):
                come_results.append(("win", initial_come_bet))
                total_come_bets -= initial_come_bet
            elif come_roll in (2, 3, 12):
                come_results.append(("lose", initial_come_bet))
                total_come_bets -= initial_come_bet
            else:
                active_come_bets[come_roll] = initial_come_bet

        sum2 = 0
        while True:
            sum2 = dice_roll()
            new_come_bet = choose_come_bet(balance, total_come_bets)
            if new_come_bet > 0:
                if balance >= new_come_bet:
                    balance -= new_come_bet
                    if sum2 in (7, 11):
                        come_results.append(("win", new_come_bet))
                        total_come_bets -= new_come_bet
                    elif sum2 in (2, 3, 12):
                        come_results.append(("lose", new_come_bet))
                        total_come_bets -= new_come_bet    
                    else:
                        active_come_bets[sum2] = new_come_bet
                else:
                    pass  # nicht genug Balance für neuen Come-Bet
                
            # Prüfen, ob eine aktive Come-Wette getroffen wird
            if sum2 in active_come_bets:
                result = active_come_bets.pop(sum2)
                come_results.append(("win", result))
                total_come_bets -= result
            
            if sum2 == point:
                passline = "win"
                dpassline = "lose"
                break
            elif sum2 == 7:
                passline = "lose"
                dpassline = "win"
                come_results += [("lose", bet) for bet in active_come_bets.values()]
                active_come_bets.clear()
                break
    

    return auswertung(balance, passline, dpassline, come_results, passbet, dpassbet), passline, dpassline, come_results

def choose_come_bet(balance, total_come_bets):
    return 0

def crapsmitmontecarlo(iterationen, filename="craps_results.csv"):
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Versuch", "Passline", "Don't Passline", "Come Ergebnisse", "Balance nach Spiel"])
        
        
        balance_gesamt = 0
        anzahl_durchläufe = 0
        for i in range(1, iterationen + 1):
            balance = 1
        
            passbet = 0
            dpassbet = 0
            initial_come_bet = 1  # Erster Come-Bet Betrag
        
        
            balance, passline, dpassline, come_results = game(balance, passbet, dpassbet, initial_come_bet)
            
            if balance != 1:
                writer.writerow([i, passline, dpassline, come_results, balance])
                balance_gesamt += balance
                anzahl_durchläufe += 1
        
        print("House Edge", (1 - balance_gesamt/anzahl_durchläufe)*100)