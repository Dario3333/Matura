import random
import csv

def dice_roll():
    return random.randint(1, 6) + random.randint(1, 6) #Simuliert 2 würfel und addiert sie zusammen

def game(balance, passbet, dont_passbet):
    passline = ""
    dont_passline = ""
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
        
        while True: #Würfeln bis Point wieder getroffen wird oder eine 7 gewürfelt wird
            roll = dice_roll()
            if roll == point:
                passline = "win"
                dont_passline = "lose"
                break
            if roll == 7:
                passline = "lose"
                dont_passline = "win"
                break
        
    return auswertung(balance, passline, passbet, dont_passline, dont_passbet)


#def chose_new_come_bet

def auswertung(balance, passline, passbet,dont_passline, dont_passbet):
    if passline == "win":
        balance += 2*passbet  #wenn gewonnen doppelt zurück sonst nicht(bet wurde am anfang schon abgezogen)
        
    if dont_passline == "win":
        balance += 2*dont_passbet
    
    if dont_passline == "push":
        balance += dont_passbet
    
    return balance

def crapsmitmontecarlo_neu(iterationen):
    balance_ges = 0
    
    for i in range(1, iterationen + 1):
        balance = 10
        
        #Wetten gesetzt
        passbet = 0 
        balance -= passbet
        
        dont_passbet = 1
        balance -= dont_passbet
    
        balance = game(balance, passbet, dont_passbet)
        balance_ges += balance
    
    print("House-Edge:", (10-(balance_ges/iterationen))*100,"%")