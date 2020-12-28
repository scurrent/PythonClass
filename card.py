# This is a sample Python script.

class Card :
    suits = ["Hearts", "Diamonds," "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self) :
        return f"{self.value} of {self.suit}"