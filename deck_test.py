import unittest
from card import Card
from deck import Deck



class CardTests(unittest.TestCase):
    suits = ["Hearts", "Diamonds," "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def setUp(self):
        print(" in setup")
        self.test_card = Card("Hearts", "2")

    def test_card(self):
        print("test shuffle")
        self.assertIsInstance(self.test_card, Card)
        self.assertIn(self.test_card.suit, ["Hearts", "Diamonds," "Clubs", "Spades"])
        self.assertIn(self.test_card.value, ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

    def test_repr(self):
        self.assertEqual(repr(self.test_card), "2 of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        print(" in setup")
        self.test_deck = Deck()

    def test_shuffle(self):
        print("test shuffle")
        self.test_deck.shuffle()
        self.assertEqual(self.test_deck.count(), 52)

    def test_count(self):
        print("test count")
        self.assertEqual(self.test_deck.count(), 52)
        self.test_deck.cards.pop()
        self.assertEqual(self.test_deck.count(), 51)

    def test_deal_card(self):
        print(" test deal card")
        result = self.test_deck.deal_card()
        self.assertIsInstance(result, Card)

    def test_deal_hand(self):
        print(" test say name")
        result = self.test_deck.deal_hand(6)
        self.assertEqual(len(result), 6)

    def tearDown(self) :
        print(" test tearDown")


if __name__ == "__main__":
    unittest.main()
