
from card import Card
import random

def drawCard():
    cardToDraw = random.randint(0, len(deck)-1)
    card = deck[cardToDraw]
    deck.pop(cardToDraw)
    return card

def findHandValue(hand):
    score = 0
    for card in hand:
        score += card.score
    return score


deck = []
for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
    for i in range(1, 14):
        deck.append(Card(suit=suit, value=i))

playerHand = []
playerHand.append(drawCard())
playerHand.append(drawCard())

#check for blackjack
if playerHand[0].value == 'A':
    if playerHand[1].score == 10:
        for card in playerHand:
            card.draw()
        print("Blackjack! You win!")
        quit()
if playerHand[1].value == 'A':
    if playerHand[0].score == 10:
        for card in playerHand:
            card.draw()
        print("Blackjack! You win!")
        quit()

cpuHand = []
cpuHand.append(drawCard())
cpuHand.append(drawCard())


while True:
    for card in playerHand:
        card.draw()
    choice = input("Would you like another card? Y or N  ").upper()
    if choice == 'Y':
        playerHand.append(drawCard())
    else:
        break

#Handle CPU  Hand
#Say they draw a card if hand < 15 otherwise stick
while findHandValue(cpuHand) <= 14:
    cpuHand.append(drawCard())

for card in playerHand:
    if card.value == 'A':
        high = input(f"Count the Ace of {card.suit} as high? Y or N ").upper()
        if high == 'Y':
            card.score = 11

if findHandValue(playerHand) > 21:
    print("Your hand value went over 21, computer wins")
elif findHandValue(cpuHand) > 21:
    print("Computers hand value went over 21, you win")
elif len(cpuHand) > 4:
    print("Computer has five or more cards, so they win!")
elif len(playerHand) > 4:
    print("You have five or more cards, so you win!")
elif findHandValue(playerHand) > findHandValue(cpuHand):
    print("Player wins!")
elif findHandValue(playerHand) < findHandValue(cpuHand):
    print("Computer wins!")
else:
    print("it's a draw")

