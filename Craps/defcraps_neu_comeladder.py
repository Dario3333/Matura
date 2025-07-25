import random
import csv

def dice_roll():
    return random.randint(1, 6) + random.randint(1, 6) #Simuliert 2 würfel und addiert sie zusammen

def game(balance, passbet, dont_passbet, initial_comebet, active_come_bets):
    passline = ""
    dont_passline = ""
    come_results = []   #zum alle Ergebnise eintragen, einfacher zum auswerten
    total_come_bets = 0 #insgesamt eingesetztes Geld zählen für die House-Edge Rechnung
    come_out_roll = dice_roll() #erster roll
    #print("come_out roll:", come_out_roll)
    
    if come_out_roll in active_come_bets:   #prüfen ob eine aktive come bet getroffen wird und dadurch gewinnt
        result = active_come_bets.pop(come_out_roll)
        come_results.append(("win", result))
        #print("win", come_out_roll, result)
    
    if come_out_roll in (7, 11): #direkt gewonnen/verloren
        passline = "win"
        dont_passline = "lose"
        if come_out_roll == 7:
            active_come_bets.clear() #alle aktiven come bets verlieren
        
    
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
        total_come_bets += new_come_bet
        #print("bet:", new_come_bet)
        #print("balance:", balance)



        first = True
        
        while True: #Würfeln bis Point wieder getroffen wird oder eine 7 gewürfelt wird
            if not first: #neue come bets werden erst beim 2. Mal gemacht
                if balance > 0:
                    new_come_bet = chose_new_come_bet(active_come_bets)  #neue come bet setzen
                    balance -= new_come_bet
                    total_come_bets += new_come_bet
                    #print("bet:", new_come_bet)
                    #print("balance:", balance)
                else:
                    new_come_bet = 0
            
            roll = dice_roll()
            #print("roll:", roll)
            
            if roll in active_come_bets:   #prüfen ob eine aktive come bet getroffen wird und dadurch gewinnt
                result = active_come_bets.pop(roll)
                come_results.append(("win", result))
                #print("win", roll, result)
            
            #prüfen ob come bet direkt gewinnt oder verliert, sonst zu aktven come bets hinzufügen
            if roll in (7, 11):
                come_results.append(("win", new_come_bet))
                #print("direct win")
            elif roll in (2, 3, 12):
                come_results.append(("lose", new_come_bet))
                #print("direct loss")
            else:
                active_come_bets[roll] = new_come_bet
                #print("point established")
                 
                 
                 
            if roll == point:
                passline = "win"
                dont_passline = "lose"
                break
            
            if roll == 7:
                passline = "lose"
                dont_passline = "win"
                active_come_bets.clear() #alle aktiven come bets verlieren
                break
            
            first = False
              
    return auswertung(balance, passline, passbet, dont_passline, dont_passbet, come_results), total_come_bets, active_come_bets


def chose_new_come_bet(active_come_bets):
    x = 0
    for roll, bet in active_come_bets.items():
       x+= bet
    x += 1
    if x > 20:
        return 0
    else:
        return x

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

def crapsmitmontecarlo_neu(iterationen, filename="craps_results.csv"):
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Versuch", "Gewinn", "Balance nach Runde", "House-Edge nach Runde"])
    
    
        total_bets = 0
        active_come_bets = {} #come bets tracken
        balance = 10000000
    
        for i in range(1, iterationen + 1):
        
            #Wetten gesetzt
            passbet = 0
            balance -= passbet
        
            dont_passbet = 0
            balance -= dont_passbet
        
            initial_comebet = 1
            balance_bevor = balance
    
            balance, all_come_bets, active_come_bets = game(balance, passbet, dont_passbet, initial_comebet, active_come_bets)
            #print("active_come_bets:", active_come_bets) 
            #print("balance:", balance)
            total_bets += (passbet  + dont_passbet + all_come_bets)
            #print("total bets:", total_bets)
            
            if i % 1 == 0 and total_bets != 0:
                house_edge = ((10000000-balance)/total_bets*100)
                writer.writerow([i, balance - balance_bevor, balance, house_edge])
            elif i % 1 == 0:
                writer.writerow([i, balance - balance_bevor, balance, "no bets"])
            
    
        #print("active_come_bets:",active_come_bets)
        #print("total bets:", total_bets)
            

        print("House edge:", (10000000-balance)/total_bets*100)
        return ((10000000-balance)/total_bets*100)
    
        #print("balance:", balance)
        #print("iterationen:", iterationen)


