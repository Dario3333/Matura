import random


def dice_roll():
    x = random.randint(0,6) + random.randint(0,6)
    return x


def craps():
    sum = dice_roll()
    if sum == 7 or sum == 11:
        ergebnis = 1
    elif sum == 2 or sum == 3 or sum == 12:
        ergebnis = 0
    else:
        s2 = 0
        while s2 != sum and s2 != 7:
            s2 = dice_roll()
        if s2 == 7:
            return 0
        else:
            return 1
        
    return ergebnis


ergebnis = craps()

if ergebnis == 1:
    print("Pass line wins")
else:
    print("don't pass line wins")
