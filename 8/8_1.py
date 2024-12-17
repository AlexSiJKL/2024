import os.path

filename = "8.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

data = {}
i = 0
j = 0

try:
    with open(os.path.join(path, filename), "r") as file:
        lines = file.readlines()
        i = len(lines)
        j = max(len(line.strip()) for line in lines)
        
        for row_idx, line in enumerate(lines):
            for col_idx, char in enumerate(line.strip()):
                if char != '.':
                    data[(row_idx, col_idx)] = char
except Exception as e:
    print("Failed to read file:", e)

print("Dictionary with character coordinates:", data)
print("Number of rows (i):", i)
print("Maximum row length (j):", j)

# Creating a dictionary to hold coordinates for each unique character
char_coordinates = {}
for key, value in data.items():
    if value not in char_coordinates:
        char_coordinates[value] = []
    char_coordinates[value].append(key)

# Update coordinates for each unique character
def update_coordinates(coordinates, data_dict, rows, cols):
    for idx1 in range(len(coordinates)):
        for idx2 in range(idx1 + 1, len(coordinates)):
            # First coordinate
            x1, y1 = coordinates[idx1]
            # Second coordinate
            x2, y2 = coordinates[idx2]
            
            # Calculate new coordinates for '#'
            new_x1 = x1 - (x2 - x1)
            new_y1 = y1 - (y2 - y1)
            new_x2 = x2 - (x1 - x2)
            new_y2 = y2 - (y1 - y2)
            
            # Update the data dictionary
            for new_x, new_y in [(new_x1, new_y1), (new_x2, new_y2)]:
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    # Check if '#' already exists
                    if (new_x, new_y) not in data_dict:
                        data_dict[(new_x, new_y)] = '#'  # Add '#' for the coordinate
                    elif data_dict[(new_x, new_y)] != '#':
                        # If there's already a different character, convert to tuple
                        if isinstance(data_dict[(new_x, new_y)], tuple):
                            # If already a tuple, append '#'
                            data_dict[(new_x, new_y)] = (data_dict[(new_x, new_y)][0], '#')
                        else:
                            # Otherwise, create a tuple with the existing char and '#'
                            data_dict[(new_x, new_y)] = (data_dict[(new_x, new_y)], '#')

# Iterate over each character and update coordinates
for char, coordinates in char_coordinates.items():
    update_coordinates(coordinates, data, i, j)

print("Updated dictionary with '#' coordinates:", data)

# Count the number of '#' in the updated data
hash_count = sum(1 for value in data.values() if value == '#' or (isinstance(value, tuple) and '#' in value))

print("Number of '#' in the updated data:", hash_count)
