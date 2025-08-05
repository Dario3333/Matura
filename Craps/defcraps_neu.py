import random
import csv

def dice_roll():
    return random.randint(1, 6) + random.randint(1, 6) #Simuliert 2 würfel und addiert sie zusammen

def game(balance, passbet, dont_passbet, initial_comebet, initial_dont_comebet, active_come_bets, active_dont_come_bets):
    passline = ""
    dont_passline = ""
    come_results = []   #zum alle Ergebnise eintragen, einfacher zum auswerten
    dont_come_results = [] #gleich wie oben einfach für dont come
    total_come_bets = 0 #insgesamt auf come und don't come bet gesetzte Chips zählen für House-Edge rechnung
    come_out_roll = dice_roll() #erster roll
    
    if come_out_roll in active_come_bets:   #prüfen ob eine aktive come bet getroffen wird und dadurch gewinnt
        result = active_come_bets.pop(come_out_roll)
        come_results.append(("win", result))
        
        if come_out_roll in active_dont_come_bets:   #prüfen ob eine aktive don't come bet getroffen wird und dadurch verliert
            active_dont_come_bets.pop(come_out_roll)
            
    
    if come_out_roll in (7, 11): #direkt gewonnen/verloren
        passline = "win"
        dont_passline = "lose"
        if come_out_roll == 7:
            active_come_bets.clear() #alle aktiven come bets verlieren
            for roll, bet in active_dont_come_bets.items():
                dont_come_results.append(("win", bet))
            active_dont_come_bets.clear()
            
        
    
    elif come_out_roll in (2,3):  #direkt gewonnen/verloren
        passline = "lose"
        dont_passline = "win"
    
    elif come_out_roll == 12:   #passline verloren, dont passline unentschieden
        passline = "lose"
        dont_passline = "push"
        
    else:
        point = come_out_roll #come out roll wird zum Point
        new_come_bet = initial_comebet #come bet setzen
        balance -= new_come_bet #initial_come_bet wird erst abgezogen wenn auch eine come bet ausgeführt wird
        new_dont_come_bet = initial_dont_comebet #don't come bet setzen
        balance -= new_dont_come_bet #initial_dont_come_bet wird erst abgezogen wenn auch eine come bet ausgeführt wird
        total_come_bets += new_come_bet
        total_come_bets += new_dont_come_bet


        first = True
        
        while True: #Würfeln bis Point wieder getroffen wird oder eine 7 gewürfelt wird
            if not first: #neue come bets werden erst beim 2. Mal gemacht
                if balance > 0:
                    new_come_bet = chose_new_come_bet(active_come_bets)  #neue come bet setzen
                    balance -= new_come_bet
                    total_come_bets += new_come_bet
                    new_dont_come_bet = chose_new_dont_come_bet(active_dont_come_bets)  #neue don't come bet setzen
                    balance -= new_dont_come_bet
                    total_come_bets += new_dont_come_bet
                else:
                    new_come_bet = 0
                    new_dont_come_bet = 0
            roll = dice_roll()
            
            if roll in active_come_bets:   #prüfen ob eine aktive come bet getroffen wird und dadurch gewinnt
                result = active_come_bets.pop(roll)
                come_results.append(("win", result))
                
            if roll in active_dont_come_bets:   #prüfen ob eine aktive don't come bet getroffen wird und dadurch verliert
                active_dont_come_bets.pop(roll)
            
            #prüfen ob come bet direkt gewinnt oder verliert, sonst zu aktven come bets hinzufügen
            if roll in (7, 11):
                come_results.append(("win", new_come_bet))
                dont_come_results.append(("lose", new_dont_come_bet))
            elif roll in (2, 3):
                come_results.append(("lose", new_come_bet))
                dont_come_results.append(("win", new_dont_come_bet))
            elif roll == 12:
                come_results.append(("lose", new_come_bet))
                dont_come_results.append(("push", new_dont_come_bet))
            else:
                active_come_bets[roll] = new_come_bet
                active_dont_come_bets[roll] = new_dont_come_bet
                 
                 
            if roll == point:
                passline = "win"
                dont_passline = "lose"
                break
            
            if roll == 7:
                passline = "lose"
                dont_passline = "win"
                active_come_bets.clear() #alle aktiven come bets verlieren
                for roll, bet in active_dont_come_bets.items():#alle aktiven don't come bets gewinnen
                    dont_come_results.append(("win", bet))
                active_dont_come_bets.clear()
                break
            
            first = False
              
    return auswertung(balance, passline, passbet, dont_passline, dont_passbet, come_results, dont_come_results), total_come_bets, active_come_bets, active_dont_come_bets


def chose_new_come_bet(active_come_bets):
    return 1

def chose_new_dont_come_bet(active_come_bets):
    return 0



def auswertung(balance, passline, passbet,dont_passline, dont_passbet, come_results, dont_come_results):
    if passline == "win":
        balance += 2*passbet  #wenn gewonnen doppelt zurück sonst nicht(bet wurde am anfang schon abgezogen)
        
    if dont_passline == "win":
        balance += 2*dont_passbet
    
    if dont_passline == "push":
        balance += dont_passbet
    
    
    for result, bet in come_results:
        if result == "win":
            balance += 2*bet  #jeder Gewinn wird doppelt zurückgezahlt
    
    for result, bet in dont_come_results:
        if result == "win":
            balance += 2*bet  #jeder Gewinn wird doppelt zurückgezahlt
        elif result == "push":
            balance += bet #bei Unentschieden Einsatz zurückgezahlt
    
    return balance

def crapsmitmontecarlo_neu_dont(iterationen, filename="craps_results.csv"):
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Versuch", "Gewinn", "Balance nach Runde", "House-Edge nach Runde"])
    
    
        total_bets = 0
        active_come_bets = {} #come bets tracken
        active_dont_come_bets = {}
        balance = 10000000
    
        for i in range(1, iterationen + 1):
        
            #Wetten gesetzt
            passbet = 0
            balance -= passbet
        
            dont_passbet = 0
            balance -= dont_passbet
        
            initial_comebet = 1
            
            initial_dont_comebet = 0
            
            balance_bevor = balance
    
            balance, all_come_bets, active_come_bets, active_dont_come_bets = game(balance, passbet, dont_passbet, initial_comebet, initial_dont_comebet, active_come_bets, active_dont_come_bets)
            total_bets += (passbet  + dont_passbet + all_come_bets)
            
            if i % 100 == 0 and total_bets != 0:
                house_edge = ((10000000-balance)/total_bets*100)
                writer.writerow([i, balance - balance_bevor, balance, house_edge])
            elif total_bets == 0:
                writer.writerow([i, balance - balance_bevor, balance, "no bets"])
            
                

        print("House edge:", (10000000-balance)/total_bets*100)
        return ((10000000-balance)/total_bets*100)
    
        




