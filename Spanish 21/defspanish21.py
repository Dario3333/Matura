import random

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


def bets(balance):
    bet = int(input("Wie viel möchtest du setzen?"))
    balance = balance - bet
    print("you still have:",balance)
    if balance < 0:
        print("Zu wenig Geld")
        exit()
    else:
        return bet


def payout(player_hand, dealer_hand, bet, balance):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if player_value > 21:
        print("You lose")
        return balance - bet
    elif dealer_value > 21 or player_value > dealer_value:
        print("You win")
        return balance + bet
    elif player_value < dealer_value:
        print("You lose")
        return balance - bet
    else:
        print("It's a tie")
        return balance


def einzahlen():
    balance = int(input("Wie viel Geld möchtest du einzahlen? "))
    return balance
