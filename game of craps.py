import random


def dice_roll():
    x = random.randint(0,6) + random.randint(0,6)
    return x


def craps():
    balance = int(input("Wie viel Geld möchtest du einzahlen? "))
    
    passline = int(input("Wie viel möchtest du auf die Pass Line setzen? "))
    balance = balance - passline
    dpassline = int(input("Wie viel möchtest du auf die don't Pass Line setzen? "))
    balance = balance - dpassline
    
    
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
        
    if ergebnis == 1:
        passline = passline*2
        dpassline = 0
        balance = balance + passline
    else:
        dpassline = dpassline*2
        passline = 0
        balance = balance + dpassline
    
    print("Du hast", balance)


craps()
