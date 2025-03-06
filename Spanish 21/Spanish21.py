import random

# Spanish 21 uses a standard deck but without 10s
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

def play_spanish_21():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    print("Your hand:", player_hand)
    print("Dealer shows:", dealer_hand[0])
    
    while True:
        action = input("Do you want to hit or stand? (h/s): ")
        if action.lower() == 'h':
            player_hand.append(deck.pop())
            print("Your hand:", player_hand)
            if calculate_hand_value(player_hand) > 21:
                print("Bust! You lose.")
                return
        else:
            break
    
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    print("Dealer's hand:", dealer_hand)
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_spanish_21()
