""" ###`Q-2:` Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

* The `Deck` class should have a deal method to deal a single card from the deck
* After a card is dealt, it is removed from the deck.
* There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
* The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

`Deck` Class
* It is class of all possible cards in a deck. Total 52 cards.
* Methods - `deal()` it will take out one card from the deck of cards.
* Deck of cards should get shuffeled while creating the deck object.
* `no of cards remaining in deck - <number>` should dsiplay on printing any deck object.

`Card` class
* It is a class of card
* Atrributes - `suit` and `value`
* `<suit> of <value>` should dsiplay on printing any card object.
 """

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit} of {self.value}"


class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

        self.shuffle()

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def __str__(self):
        return f"No of cards remaining in deck - {len(self.cards)}"


# Create a deck
deck = Deck()

# Print the deck
print(deck)

# Deal one card
card = deck.deal()
print("Dealt card:", card)

# Print the deck after dealing
print(deck)

# Shuffle the deck again
deck.shuffle()
print("After shuffling:", deck)
