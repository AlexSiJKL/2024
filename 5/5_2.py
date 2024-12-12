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

second_chance_list = []

for item in update:
    if 1 in item:
        second_chance_list.append(item[1])

print("Before sorting:", second_chance_list)

# Sort elements in second_chance_list based on rules
for index in range(len(second_chance_list)):
    sorted = False  # Flag to check if a sorting pass is needed
    while not sorted:
        sorted = True  # Assume sorted unless we find a pair to swap
        for j in range(len(second_chance_list[index])):
            first_number = second_chance_list[index][j]
            for k in range(j + 1, len(second_chance_list[index])):
                second_number = second_chance_list[index][k]
                if (second_number, first_number) in rules:
                    # If we find that second_number should come before first_number
                    second_chance_list[index].pop(k)  # Remove second_number
                    second_chance_list[index].insert(j, second_number)  # Insert it before first_number
                    sorted = False  # Mark that we made a change, we need another pass
                    break  # Restart checking from the start of the inner loop
            if not sorted:  # If we already made a swap, we don't need to check further
                break

print("After sorting:", second_chance_list)

total_sum = 0

for line in second_chance_list:
    total_sum += line[len(line) // 2]

print(total_sum)