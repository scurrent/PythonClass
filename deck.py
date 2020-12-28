# This is a sample Python script.
from card import Card
from random import shuffle

class Deck :
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]
        print(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {self.count} cards"

    def _deal(self, num):
        count = self.count()
        remcount = min([count, num])
        print(f"Going to remove {remcount} cards")
        if remcount == 0:
            raise ValueError("Deck has no cards left")
        #use slice
        cards = self.cards[-remcount:]
        self.cards = self.cards[:-remcount]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, handsize):
        return self._deal(handsize)

    def shuffle(self):
        print(f"Deck size on shuffle {self.count()}")
        if self.count() < 52 :
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)




d = Deck()

d.shuffle()
#requires __iter__
#for card in d:
#    print(card)

card = d.deal_card()
#print(card)
hand = d.deal_hand(5)
#print(hand)
#print(d)
