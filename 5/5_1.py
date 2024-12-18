import os.path

filename = "5.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

# Initialize lists for rules and updates
rules = []
update = []

try:
    with open(os.path.join(path, filename), "r") as file:
        # Read the first lines for rules
        for line in file:
            line = line.strip()  # Remove leading and trailing whitespace
            if not line:  # Skip empty lines
                continue
            
            if '|' in line:
                left, right = line.split('|')
                rules.append((int(left), int(right)))
            else:
                # If this line is for updating (update)
                numbers = list(map(int, line.split(',')))
                update.append(numbers)

except Exception as e:
    print("Failed to create file for int:", e)

# Convert update to a list of dictionaries
update = [{0: sublist} for sublist in update]

# Check conditions and update keys
for i in range(len(update)):
    sublist = update[i][0]  # Get the sublist from the dictionary
    found = False  # Flag to track if a match is found
    for j in range(len(sublist)):
        first_number = sublist[j]
        for k in range(j + 1, len(sublist)):
            second_number = sublist[k]
            if (second_number, first_number) in rules:
                found = True  # Set flag to True if a match is found
                break  # Stop further checks for this row
        if found:
            break  # If a match is found, exit the outer loop
    if found:
        update[i][1] = update[i].pop(0)  # Change the key from 0 to 1

# Sum all middle elements (by index) of lists with key 0
total_sum = 0

for item in update:
    if 0 in item:  # Check if key 0 exists
        sublist = item[0]  # Get the sublist
        if sublist:  # Ensure the sublist is not empty
            middle_index = len(sublist) // 2  # Index of the middle element
            average = sublist[middle_index]  # Get the middle element by index
            total_sum += average  # Add to the total sum

print("Sum of all middle elements by index from lists with key 0:", total_sum)