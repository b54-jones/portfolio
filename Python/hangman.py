import requests
lives = 10
board = []

r = requests.get("https://random-word-api.herokuapp.com/word")
word = r.text[2:-2]

for letter in word:
    board.append('_')
i = 0

while(True):
    print(''.join(board))
    guess = (input("Guess a letter: ")).lower()

    if guess not in word: 
        lives = lives - 1
        print(f"Careful! Only {lives} lives left! ")
    while i < len(word):
        if word[i] == guess:
            board[i] = guess
        i = i+1
    i = 0
    if '_' not in board:
        print(f"Winner!! The word was {word}")
        break
    if lives == 0: 
        print("You ran out of lives")
        break