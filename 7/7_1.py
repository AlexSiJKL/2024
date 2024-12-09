import os.path
from itertools import product

# Open and read the input file
filename = "7.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

with open(os.path.join(path, filename), "r") as file:
    data = file.read().splitlines()

total_sum = 0  # Final sum

# Process each line of the input
for line in data:
    # Split the line into the number before ':' and the list of numbers after ':'
    parts = line.split(':')
    
    base_number = int(parts[0])  # The number before ':'
    numbers = list(map(int, parts[1].strip().split()))  # The numbers after ':'

    # Generate all combinations of operators for the given list of numbers
    operators = ['+', '*']
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    
    # Iterate through all operator combinations
    for combo in operator_combinations:
        # Evaluate the expression left to right
        result = numbers[0]  # Start with the first number
        for idx, op in enumerate(combo):
            if op == '+':
                result += numbers[idx + 1]  # Perform addition
            elif op == '*':
                result *= numbers[idx + 1]  # Perform multiplication

        # Check if the result matches the base number
        if result == base_number:  # Compare with the number before ':'
            total_sum += base_number  # Add the base number to the sum
            break

print(total_sum)