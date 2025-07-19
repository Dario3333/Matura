import random
import csv

def dice_roll():
    return random.randint(1, 6) + random.randint(1, 6) #Simuliert 2 würfel und addiert sie zusammen

def game(balance, passbet, dont_passbet, initial_comebet):
    passline = ""
    dont_passline = ""
    come_results = []   #zum alle Ergebnise eintragen, einfacher zum auswerten
    total_come_bets = 0 #insgesamt eingesetztes Geld zählen für die House-Edge Rechnung
    come_out_roll = dice_roll() #erster roll
    
    if come_out_roll in (7, 11): #direkt gewonnen/verloren
        passline = "win"
        dont_passline = "lose"
        
    
    elif come_out_roll in (2,3):  #direkt gewonnen/verloren
        passline = "lose"
        dont_passline = "win"
    
    elif come_out_roll == 12:   #passline verloren, dont passline unentschieden
        passline = "lose"
        dont_passline = "push"
        
    else:
        point = come_out_roll #come out roll wird zum Point
        active_come_bets = {} #come bets tracken
        total_come_bets += initial_comebet 
        new_come_bet = initial_comebet #come bet setzen



        first = True
        
        while True: #Würfeln bis Point wieder getroffen wird oder eine 7 gewürfelt wird
            if not first: #neue come bets werden erst beim 2. Mal gemacht
                if balance > 0:
                    new_come_bet = chose_new_come_bet()  #neue come bet setzen
                    balance -= new_come_bet
                    total_come_bets += new_come_bet
                else:
                    new_come_bet == 0
            
            roll = dice_roll()
            #prüfen ob come bet direkt gewinnt oder verliert, sonst zu aktven come bets hinzufügen
            if roll in (7, 11):
                come_results.append(("win", new_come_bet))
            elif roll in (2, 3, 12):
                come_results.append(("lose", new_come_bet))
            else:
                active_come_bets[roll] = new_come_bet
                 
                 
            if roll in active_come_bets:   #prüfen ob eine aktive come bet getroffen wird und dadurch gewinnt
                result = active_come_bets.pop(roll)
                come_results.append(("win", result))
                active_come_bets.pop(roll, None)
                 
            if roll == point:
                passline = "win"
                dont_passline = "lose"
                break
            if roll == 7:
                passline = "lose"
                dont_passline = "win"
                for _, bet in active_come_bets.items():
                    come_results.append(("lose", bet))
                break
            
            first = False
            
            
    return auswertung(balance, passline, passbet, dont_passline, dont_passbet, come_results), total_come_bets


def chose_new_come_bet():
    return 0

def auswertung(balance, passline, passbet,dont_passline, dont_passbet, come_results):
    if passline == "win":
        balance += 2*passbet  #wenn gewonnen doppelt zurück sonst nicht(bet wurde am anfang schon abgezogen)
        
    if dont_passline == "win":
        balance += 2*dont_passbet
    
    if dont_passline == "push":
        balance += dont_passbet
    
    
    for result, bet in come_results:
        if result == "win":
            balance += 2*bet  #jeder Gewinn wird doppelt zurückgezahlt
    
    return balance

def crapsmitmontecarlo_neu(iterationen):
    balance_ges = 0
    total_bets = 0
    
    for i in range(1, iterationen + 1):
        balance = 10
        
        #Wetten gesetzt
        passbet = 0
        balance -= passbet
        
        dont_passbet = 0
        balance -= dont_passbet
        
        initial_comebet = 1
        balance -= initial_comebet
    
        balance, all_come_bets = game(balance, passbet, dont_passbet, initial_comebet)
        balance_ges += balance
        total_bets += (passbet  + dont_passbet + all_come_bets)
    
    print("House-Edge 1:", (10-(balance_ges/iterationen))*100,"%") #House-Edge nach Formel (Verlust/Einsatz)*100
    print("House-Edge 2:", (10*iterationen - balance_ges)/(10*iterationen)*100)

