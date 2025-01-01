import random


def dice_roll():
    x = random.randint(0,6) + random.randint(0,6)
    return x


def craps():
    balance = int(input("Wie viel Geld möchtest du einzahlen? "))
    
    #Wetten machen
    passline = int(input("Wie viel möchtest du auf die Pass Line setzen? "))
    balance = balance - passline
    
    dpassline = int(input("Wie viel möchtest du auf die don't Pass Line setzen? "))
    balance = balance - dpassline
    
    fieldbet = int(input("Wie viel möchtest du auf die Field Bet setzen? "))
    balance = balance - fieldbet
    
    
    
    
    #Spiel
    sum = dice_roll()
    print("Der come out roll ist: ", sum)
    
    if sum == 7 or sum == 11:
        ergebnis = 1
        
    elif sum == 2 or sum == 3 or sum == 12:
        ergebnis = 0
        
    else:
        s2 = 0
        x = 1
        while s2 != sum and s2 != 7:
            s2 = dice_roll()
            print("Der", x, ". Wurf ist: ", s2)
            x = x+1
        if s2 == 7:
            ergebnis = 0
        else:
            ergebnis = 1
     
     
    #Auszahlung    
    if ergebnis == 1:
        balance = balance + passline*2
    else:
        balance = balance + dpassline*2
        
    if sum == 2 or sum == 3 or sum == 4 or sum == 9 or sum == 10 or sum == 11 or sum == 12:
        if sum == 2:
            balance = balance + fieldbet*3
        elif sum == 12:
            balance = balance + fieldbet*4
        else:
            balance = balance + fieldbet*2
    
    print("Du hast", balance)


craps()
