#!/usr/bin/env python3
# Write a function print_fibonacci() that prints a list of the fibonacci sequenceLinks to an external site. up to the length provided in the function's parameters.

# => [0, 1, 1, 2, 3, 5, 8, 13, 21]

# fibonacci series - Each number is equal to the sum of the preceding two numbers. 

def print_fibonacci(length):
    

    fibonacci_sequence = [0,1]

    if length <= 0:
        print([])
        return
    
    while len(fibonacci_sequence) < length:
        next_fibonancci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonancci)

    print(fibonacci_sequence[:length])

print_fibonacci(0)