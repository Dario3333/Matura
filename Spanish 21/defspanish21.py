import random
import csv

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
    deck = [{'value': v, 'suit': s} for s in suits for v in values]
    random.shuffle(deck)
    return deck


def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card['value'] in ['J', 'Q', 'K']:
            value += 10
        elif card['value'] == 'A':
            aces += 1
            value += 11
        else:
            value += int(card['value'])
    
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value



def payout(player_hand, dealer_hand, bet, balance):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if player_value > 21:
        print("You lose")
        return balance - bet
    elif dealer_value > 21 or player_value > dealer_value:
        print("You win")
        if player_value == 21:
            if len(player_hand) == 6:
                return balance + 2*bet
            elif len(player_hand) == 7:
                return balance + 3*bet
            else:
                return balance + 3/2*bet
        else:
            return balance + bet
    elif player_value < dealer_value:
        print("You lose")
        return balance - bet
    else:
        print("It's a tie")
        return balance




def spanish21mitmontecarlo(iterationen):

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
        gewinn = balance - bet
    
        data.append([gewinn])
        print(f"Versuch {i + 1}: Gewinn = {gewinn}")

     #CSV-Datei schreiben
    with open("gewinne.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Gewinn"])
        writer.writerows(data)

