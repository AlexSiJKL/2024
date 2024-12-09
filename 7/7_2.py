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
    operators = ['+', '*', '||']  # Include the concatenation operator
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    
    # Iterate through all operator combinations
    for combo in operator_combinations:
        # Start with the first number as a string for concatenation
        result = str(numbers[0])  
        
        # Evaluate the expression left to right
        for idx, op in enumerate(combo):
            if op == '+':
                result = str(int(result) + numbers[idx + 1])  # Perform addition
            elif op == '*':
                result = str(int(result) * numbers[idx + 1])  # Perform multiplication
            elif op == '||':
                result += str(numbers[idx + 1])  # Concatenate as string

        # Check if the result matches the base number
        if int(result) == base_number:  # Compare with the number before ':'
            total_sum += base_number  # Add the base number to the sum
            break  # Stop processing if a match is found

# Print the final result
print(total_sum)
