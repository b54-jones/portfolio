def fibonacci(n):
    index = 0
    sequence = [1, 1]
    while len(sequence) < n:
        newNumber = sequence[index] + sequence[index+1]
        sequence.append(newNumber)
        index+=1
    return sequence

print(fibonacci(10))