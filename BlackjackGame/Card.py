class Card:
    def __init__ (self, value, suit):
        self.value = value
        self.suit = suit

    def get_suit(self):
        return self.suit

    def get_value(self, isBlackJack):
        if isBlackJack:
            return self.value
        else:
            if self.value == 1:
                return 11
            elif self.value > 10:
                return 10
            else:
                return self.value

    def declare_card(self):
        if self.value == 11:
            return "the Jack of " + str(self.suit)
        elif self.value == 12:
            return "the Queen of " + str(self.suit)
        elif self.value == 1:
            return "the Ace of " + str(self.suit)
        else:
            return "the " + str(self.value) + " of " + str(self.suit)