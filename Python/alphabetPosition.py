
def alphabet_position(text):
    numbers = []
    
    for char in text.lower():
        if char not in "abcdefghijklmnopqrstuvwxyz":
            continue
        n = ord(char) - 96
        numbers.append(str(n))
    
    return " ".join(numbers)

a = alphabet_position("Hello")
print(a)