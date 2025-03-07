import random
import csv
from defspanish21 import*

iterationen = int(input("Wie viele Iterationen?"))

data = []
for i in range(iterationen):
    balance = 10
    bet = 10
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    while True:
        if calculate_hand_value(player_hand) <= 16:
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21:
                break
        else:
            break
    
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    balance = payout(player_hand, dealer_hand, bet, balance)
    gewinn = balance - 10
    
    data.append([gewinn])
    print(f"Versuch {i + 1}: Gewinn = {gewinn}")

# CSV-Datei schreiben
with open("gewinne.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Gewinn"])
    writer.writerows(data)
