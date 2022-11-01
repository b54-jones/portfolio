import random
import numpy

def genPassword():
    firstDigit = str(random.randint(0, 9))
    secondDigit = str(random.randint(0, 9))
    firstUpper = chr(random.randint(65, 90))
    secondUpper = chr(random.randint(65, 90))
    firstLower = chr(random.randint(97, 122))
    secondLower = chr(random.randint(97, 122))
    firstSymbol = chr(random.randint(33, 47))
    secondSymbol = chr(random.randint(33, 47))
    passwordInOrder = firstDigit + secondSymbol + secondDigit + firstSymbol + firstLower + secondLower + firstUpper + secondUpper
    shuffler = list(passwordInOrder)
    random.shuffle(shuffler)
    
    return ''.join(shuffler)

print(genPassword())