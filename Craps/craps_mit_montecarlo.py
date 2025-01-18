import random
from defcraps import *


def crapsmontecarlo(iterationen):
    
    wins = 0
    losses = 0
    
    for i in range (iterationen):
        
        passline = random.randint(0,1)
        if passline == 0:
            dpassline = 1
        else:
            dpassline = 0

    
    
        ergebnis = game()
     
     
  
        balance = auswertung(ergebnis, passline, dpassline)
    


        if balance == 2:
            wins = wins  + 1
        else:
            losses = losses + 1
    print("you won", wins,"times and lost", losses, "times")
    print("you won", (wins/iterationen)*100 , "% of your games")


iterationen = 10000
crapsmontecarlo(iterationen)

