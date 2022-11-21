import random
from Card import Card

class Deck:
    def __init__(self):
        pass

    def draw_card(self):
        value = random.randint(1, 13)
        cardSuit = random.randint(1, 4)
        suit = ""

        if cardSuit == 1:
            suit = "Spades"
        elif cardSuit == 2:
            suit = "Clubs"
        elif cardSuit == 3:
            suit = "Hearts"
        else:
            suit = "Diamonds"

        return Card(value, suit)