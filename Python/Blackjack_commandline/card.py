
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        if value == 1:
            self.value = 'A'
            self.score = 1
        if value in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.value = value
            self.score = value
        if value == 11:
            self.value = 'J'
            self.score = 10
        if value == 12:
            self.value = 'Q'
            self.score = 10
        if value == 13:
            self.value = 'K'
            self.score = 10
        
    def draw(self):
        print("----------")
        print(f"|{self.value}      {self.value}|")
        print("|        |")
        # find length of suit then add spaces to make it 10
        lenSuit = len(self.suit)
        emptySpaces = 7 - lenSuit
        suitString = "|" + " " + self.suit + " " * emptySpaces + "|"
        if self.suit == "Diamonds":
            suitString = "|" + self.suit + " " * emptySpaces + "|"
        print(suitString)
        print("|        |")
        print(f"|{self.value}      {self.value}|")
        print("----------")
        return 