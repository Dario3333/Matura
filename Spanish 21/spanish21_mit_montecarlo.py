import random
from defspanish21 import*

iterationen = int(input("Wie viele Iterationen?"))
for i in range (iterationen):
    balance = 10
    bet = 10
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    #print("Your hand:", player_hand)
    #print("Dealer shows:", dealer_hand[0])
    
    while True:
        if calculate_hand_value(player_hand) <= 16:
            player_hand.append(deck.pop())
            #print("Your hand:", player_hand)
            if calculate_hand_value(player_hand) > 21:
                #print("Bust!")
                break
        else:
            break
    
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    #print("Dealer's hand:", dealer_hand)
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    

    
    balance = payout(player_hand, dealer_hand, bet, balance)
    print("You have: ", balance)