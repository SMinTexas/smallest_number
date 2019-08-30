# Given a list of numbers, print the smallest of the numbers.

numbers = [7, 21, 4, 33, -456, 8, 99, 1, 12340, 2, 79, 88, 124, 90]

minimum = 0
for number in numbers:
    if number < minimum:
        minimum = number
print(f'The minimum number in the list is {minimum}')