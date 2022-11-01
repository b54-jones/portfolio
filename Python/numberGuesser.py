import random

randomNumber = random.randint(1, 10)
highScore = 0

guess = int(input("Guess your number (1-10): "))
score = 100

while (guess != randomNumber):
    if (guess > randomNumber):
        guess = int(input("Wrong! Guess a bit lower this time: "))
        score = score - 10
    if (guess < randomNumber):
        guess = int(input("Wrong! Guess a bit higher this time: "))
        score = score - 10

print(f"Game over, you scored {score} points")