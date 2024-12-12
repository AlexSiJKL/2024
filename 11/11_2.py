import os.path

filename = "11.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

data = {}

# Read data from the file and populate the dictionary with the count of occurrences
with open(os.path.join(path, filename), "r") as file:
    numbers = list(map(int, file.read().split()))
    for number in numbers:
        if number in data:
            data[number] += 1  # Increment the count if the number is already in the dictionary
        else:
            data[number] = 1  # Initialize the count for a new number

precalc_dict = {}  # Dictionary to store pre-calculated results

def Blink(data, passes):
    global precalc_dict  # Use the global precalc_dict
    for _ in range(passes):  # Repeat the process for the specified number of passes
        count_dict = {}  # Dictionary to store values for the current iteration
        
        for num, count in data.items():  # Iterate through keys and their counts in the data dictionary
            if num in precalc_dict:  # Check if the key is in the precalc_dict
                new_values = precalc_dict[num]  # Retrieve values from precalc_dict
                for value in new_values:
                    if value in count_dict:
                        count_dict[value] += count  # Add the count to the existing value in count_dict
                    else:
                        count_dict[value] = count  # Initialize the value in count_dict
            else:
                if num == 0:
                    # Process the number 0
                    count_dict[1] = count_dict.get(1, 0) + count  # Increment the count for key 1 in count_dict
                    
                    # Update precalc_dict with the result for 0
                    precalc_dict[num] = (1,)
                elif len(str(num)) % 2 == 0:  # Check if the number of digits is even
                    num_str = str(num)
                    mid = len(num_str) // 2
                    left_part = int(num_str[:mid])  # Get the left part of the number
                    right_part = int(num_str[mid:])  # Get the right part of the number
                    
                    # Add both parts to count_dict
                    count_dict[left_part] = count_dict.get(left_part, 0) + count
                    count_dict[right_part] = count_dict.get(right_part, 0) + count
                    
                    # Add the new values to precalc_dict
                    precalc_dict[num] = (left_part, right_part)
                else:
                    # If the number of digits is odd, multiply by 2024
                    value = num * 2024
                    count_dict[value] = count_dict.get(value, 0) + count  # Add the value to count_dict
                    precalc_dict[num] = (value,)  # Store the result in precalc_dict

        data = count_dict  # Update data for the next pass
        
        # Print the contents of count_dict for the current iteration (commented out for final version)
        # print(f"Iteration {_ + 1} results:", count_dict)
    
    return count_dict  # Return the final count dictionary

# Set the number of passes
passes = 75
ans = 0  # Initialize the sum accumulator
d = Blink(data, passes)  # Execute the Blink function
for key in d.keys():
    ans += d[key]  # Sum the values in the final count dictionary

print(ans)  # Print the total sum of occurrences