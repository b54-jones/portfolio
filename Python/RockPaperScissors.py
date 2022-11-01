import random
score = 0
while(True):
    print(f"Current Score: {score}")
    computer = random.choice(['paper', 'rock', 'scissors'])

    player = input('Make your choice! Paper, Rock or Scissors? ')
    player = player.lower()

    if computer == player:
        print(f"It's a tie! You both chose {player}")
    elif (player == 'paper'):
        if (computer == 'rock'):
            print("Rock covers paper, you win!")
            score = score + 1
        if (computer == 'scissors'):
            print("Scissors cuts paper, you lose!")
    elif (player == 'rock'):
        if (computer == 'paper'):
            print("Paper covers rock, you lose!")
        if (computer == 'scissors'):
            print("Rock breaks scissors, you win!")
            score = score + 1
    elif (player == 'scissors'):
        if (computer == 'rock'):
            print("Rock breaks scissors, you lose!")
        if (computer == 'paper'):
            print("Scissors cuts paper, you win!")
            score = score + 1
        else:
            print("Invalid input")
            continue
    
    keepGoing = input("Keep going? Type X to exit.")
    keepGoing = keepGoing.upper()
    if keepGoing == 'X':
        break




