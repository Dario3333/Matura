import random
import csv
from defcraps_neu import crapsmitmontecarlo_neu
from defcraps_neu_comeladder import crapsmitmontecarlo_neu_cl
from defcraps_neu_dontstrategy import crapsmitmontecarlo_neu_dont



filename = "iterationen.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["iterationen", "House-Edge"])
    
    iterationen = 100
    for i in range (100):
        house_edge = crapsmitmontecarlo_neu_dont(iterationen)
        writer.writerow([i, house_edge])
