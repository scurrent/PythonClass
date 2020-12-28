# This is a sample Python script.
from deck import Deck
import pickle

deck = Deck()
hand = deck.deal_hand(4)

with open("pickledDeck.txt", "wb") as file:
    for card in hand:
        print(card)
    pickle.dump(hand, file)

with open("pickledDeck.txt", "rb") as file:
    new_hand = pickle.load(file)
    print("Recon")
    for card in new_hand:
        print(card)

