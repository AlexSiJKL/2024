import os.path

# Load data from file
filename = "8.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

# Initialize variables
data = {}
i = 0
j = 0

try:
    with open(os.path.join(path, filename), "r") as file:
        lines = file.readlines()
        i = len(lines)  # Number of lines
        j = max(len(line.strip()) for line in lines)  # Maximum line length
        
        # Fill the dictionary with characters and their coordinates
        for row_idx, line in enumerate(lines):
            for col_idx, char in enumerate(line.strip()):
                if char != '.':  # Skip empty cells
                    data[(row_idx, col_idx)] = char
except Exception as e:
    print("Failed to read file:", e)

print("Dictionary with character coordinates:", data)
print("Number of rows (i):", i)
print("Maximum row length (j):", j)

# Create a dictionary to store coordinates of each unique character
char_coordinates = {}
for key, value in data.items():
    if value not in char_coordinates:
        char_coordinates[value] = []
    char_coordinates[value].append(key)

def update_coordinates(coordinates, data_dict, rows, cols):
    for idx1 in range(len(coordinates)):
        for idx2 in range(idx1 + 1, len(coordinates)):
            # First coordinate
            x1, y1 = coordinates[idx1]
            # Second coordinate
            x2, y2 = coordinates[idx2]

            # Step
            step_x = (x2 - x1)
            step_y = (y2 - y1)
            
            # Calculate new coordinates
            new_x1 = x1 - step_x
            new_y1 = y1 - step_y
            new_x2 = x2 + step_x
            new_y2 = y2 + step_y
            
            # Process new coordinates
            for new_x, new_y in [(new_x1, new_y1)]:
                while True:  # Start an infinite loop to update coordinates
                    # Check if out of bounds
                    if not (0 <= new_x < rows and 0 <= new_y < cols):
                        print(f"Out of bounds: ({new_x}, {new_y})")
                        break  # Exit the loop if coordinates go out of bounds

                    # Update the dictionary
                    if (new_x, new_y) not in data_dict:
                        data_dict[(new_x, new_y)] = '#'  # Add '#' for the coordinate
                    elif data_dict[(new_x, new_y)] != '#':
                        # If there is already another symbol, create a tuple
                        if isinstance(data_dict[(new_x, new_y)], tuple):
                            # If it's already a tuple, add '#'
                            data_dict[(new_x, new_y)] += ('#',)
                        else:
                            # Otherwise create a tuple with the existing symbol and '#'
                            data_dict[(new_x, new_y)] = (data_dict[(new_x, new_y)], '#')

                    # Update coordinates for the next iteration
                    new_x -= step_x  # Update new_x one step back
                    new_y -= step_y  # Update new_y one step back

            for new_x, new_y in [(new_x2, new_y2)]:
                while True:  # Start an infinite loop to update coordinates
                    # Check if out of bounds
                    if not (0 <= new_x < rows and 0 <= new_y < cols):
                        print(f"Out of bounds: ({new_x}, {new_y})")
                        break  # Exit the loop if coordinates go out of bounds

                    # Update the dictionary
                    if (new_x, new_y) not in data_dict:
                        data_dict[(new_x, new_y)] = '#'  # Add '#' for the coordinate
                    elif data_dict[(new_x, new_y)] != '#':
                        # If there is already another symbol, create a tuple
                        if isinstance(data_dict[(new_x, new_y)], tuple):
                            # If it's already a tuple, add '#'
                            data_dict[(new_x, new_y)] += ('#',)
                        else:
                            # Otherwise create a tuple with the existing symbol and '#'
                            data_dict[(new_x, new_y)] = (data_dict[(new_x, new_y)], '#')

                    # Update coordinates for the next iteration
                    new_x += step_x  # Update new_x one step forward
                    new_y += step_y  # Update new_y one step forward

# Iterate over each symbol and update coordinates
for char, coordinates in char_coordinates.items():
    update_coordinates(coordinates, data, i, j)

print("Updated dictionary with '#' coordinates:", data)

# Add '#' for coordinates of symbols that appear 2 or more times
for char, coordinates in char_coordinates.items():
    if len(coordinates) >= 2:  # If the symbol appears 2 or more times
        for coord in coordinates:
            if coord in data:
                # If the symbol already exists, add '#' to the tuple
                if isinstance(data[coord], tuple):
                    data[coord] += ('#',)  # Add '#' to the tuple
                else:
                    data[coord] = (data[coord], '#')  # Convert to tuple and add '#'
            else:
                data[coord] = '#'  # If the coordinate is not present, add '#'

# Count the number of '#' in the updated data
hash_count = sum(1 for value in data.values() if value == '#' or (isinstance(value, tuple) and '#' in value))

print("Number of '#' in the updated data:", hash_count)