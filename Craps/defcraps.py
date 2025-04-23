import random
import csv


def dice_roll():
    return random.randint(1, 6) + random.randint(1, 6)

def auswertung(balance, passline, dpassline, come, passbet, dpassbet, comebet):
    if passline == "win":
        balance += 2*passbet
    if dpassline == "win":
        balance += 2*dpassbet
    if come == "win":
        balance += 2*comebet
    if come == "tie":
        balance += comebet
    if dpassline == "push":
        balance += dpassbet
    return balance

 
    
def game(balance, passbet, dpassbet, comebet):
    
    passline = ""
    dpassline = ""
    come = ""
    sum = dice_roll()
    print(sum)
    
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
        come_roll = dice_roll()
        print(come_roll)
        if come_roll in (7,11):
            come = "win"
        elif come_roll in(2,3,12):
            come = "lose"

        if come_roll == point:
            passline = "win"
            dpassline = "lose"
        elif come_roll == 7:
            passline = "lose"
            dpassline = "win"
        else:
            sum2 = 0
            while sum2!= point and sum2 != 7:
                sum2 = dice_roll()
                print(sum2)
                if sum2 == come_roll:
                    come = "win"
        
            if sum2 == point:
                passline = "win"
                dpassline = "lose"
                if come == "":
                    come = "tie"
            else:
                passline = "lose"
                dpassline = "win"
                come = "lose"
    print(passline, dpassline, come)
    return auswertung(balance, passline, dpassline, come, passbet, dpassbet, comebet), passline, dpassline, come
    
    
def crapsmitmontecarlo(iterationen, filename="craps_results.csv"):
    wins = 0
    losses = 0
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file) 
        writer.writerow(["Versuch", "come", "Passline", "don't Passline", "Balance nach Spiel"])
    
        for i in range(1, iterationen + 1):
            balance = 10
        
            passbet = 0
            dpassbet = 0
            comebet = 1
            balance -= 1
        
            balance, passline, dpassline, come = game(balance, passbet, dpassbet, comebet)
            print(balance)
        
            writer.writerow([i, come, passline, dpassline, balance])
            
            if balance > 10:
                wins += 1
            elif balance < 10:
                losses +=1
                
    print("You won", wins, "times and lost", losses, "times")
    print("You won", (wins / iterationen) * 100, "% of your games")
    
    