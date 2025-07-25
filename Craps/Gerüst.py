import random
import csv
from defcraps_comeladder import crapsmitmontecarlo_cl
from defcraps import crapsmitmontecarlo
from defcraps_neu import crapsmitmontecarlo_neu

filename = "iterationen.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["iterationen", "House-Edge"])
    

    iterationen = 100
    for i in range (100):
        house_edge = crapsmitmontecarlo_neu(iterationen)
        writer.writerow([iterationen, house_edge])

        
