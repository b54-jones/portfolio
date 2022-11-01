import requests

r = requests.get('https://random-word-api.herokuapp.com/word?length=5')
word = r.text[2:-2]

lettersInRightPlace = []
lettersInWrongPlace = []
lettersNotInWord = []

current = ['_', '_', '_', '_', '_']
lives = 6

print(word)
while(True):
    print(current)
    print(f"Lives left: {lives}")
    print("Letters in right place: " + str(lettersInRightPlace))
    print("Letters in wrong place but in word: " + str(lettersInWrongPlace))
    print("Letters not in the word: " + str(lettersNotInWord))
    guess = input("Enter your guess now! -> ")
    while len(guess) != 5:
        guess = input("Guess must be 5 characters long!")
    x = 0
    while x < 5:
        if word[x] == guess[x]:
            current[x] = guess[x]
            if guess[x] not in lettersInRightPlace:
                lettersInRightPlace.append(guess[x])
            if guess[x] in lettersInWrongPlace:
                lettersInWrongPlace.remove(guess[x])
        elif guess[x] in word:
            if guess[x] not in lettersInWrongPlace:
                lettersInWrongPlace.append(guess[x])
        else:
            if guess[x] not in lettersNotInWord:
                lettersNotInWord.append(guess[x])
        x+=1
    lives = lives - 1

    if '_' not in current:
        print("Winner! Word was " + word)
        break;
    if lives == 0:
        print("Out of lives :(")
        print("The word was " + word)
        break;
