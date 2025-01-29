import random
import csv
from defcraps import *

def crapsmontecarlo(iterationen, filename="craps_results.csv"):
    wins = 0
    losses = 0
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Versuch", "Ergebnis"])
        
        for i in range(1, iterationen + 1):
            passline = random.randint(0, 1)
            dpassline = 1 if passline == 0 else 0

            ergebnis = game()
            balance = auswertung(ergebnis, passline, dpassline)

            if balance == 2:
                wins += 1
                writer.writerow([i, "win"])
            else:
                losses += 1
                writer.writerow([i, "loss"])
    
    print("you won", wins, "times and lost", losses, "times")
    print("you won", (wins / iterationen) * 100, "% of your games")

iterationen = 10000
crapsmontecarlo(iterationen)
