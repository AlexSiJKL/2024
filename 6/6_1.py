import os.path

filename = "6.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

try:
    with open(os.path.join(path, filename), "r") as file:
        data = [list(line) for line in file.read().splitlines()]
except Exception as e:
    print("Failed to create file for int:", e)

count = 0

is_up = True
is_right = False
is_down = False
is_left = False

def move(i, j):
    global is_down, is_left, is_right, is_up, count
    while is_down or is_left or is_right or is_up:
        if is_up:
            i, j = move_up(i, j)
        elif is_right:
            i, j = move_right(i, j)
        elif is_down:
            i, j = move_down(i, j)
        elif is_left:
            i, j = move_left(i, j)
    print(count)

def move_up(i, j):
    global is_down, is_left, is_right, is_up, count
    if i - 1 < 0:
        print(f"Out of bounds moving up from ({i}, {j}). Final count: {count}")
        is_up = False
        return i, j
    elif data[i-1][j] == '.':
        data[i-1][j] = "X"
        count += 1
        print(f"Moved up to {i-1}, {j}")
        return i-1, j
    elif data[i-1][j] == 'X':
        print(f"Moved to already marked position {i-1}, {j}")
        return i-1, j
    elif data[i-1][j] == '#':
        is_up = False
        is_right = True
        print(f"Hit # at {i-1}, {j}")
        return i, j

def move_right(i, j):
    global is_down, is_left, is_right, is_up, count
    if j + 1 >= len(data[i]):
        print(f"Out of bounds moving right from ({i}, {j}). Final count: {count}")
        is_right = False
        return i, j
    elif data[i][j+1] == '.':
        data[i][j+1] = "X"
        count += 1        
        print(f"Moved right to {i}, {j+1}")
        return i, j+1
    elif data[i][j+1] == 'X':
        print(f"Moved to already marked position {i}, {j+1}")
        return i, j+1
    elif data[i][j+1] == '#':
        is_right = False
        is_down = True
        print(f"Hit # at {i}, {j+1}")
        return i, j
    else:
        print(f"Unhandled case at {i}, {j+1}")
        return i, j

def move_down(i, j):
    global is_down, is_left, is_right, is_up, count
    if i + 1 >= len(data):
        print(f"Out of bounds moving down from ({i}, {j}). Final count: {count}")
        is_down = False
        return i, j
    elif data[i+1][j] == '.':
        data[i+1][j] = "X"
        count += 1
        print(f"Moved down to {i+1}, {j}")
        return i+1, j
    elif data[i+1][j] == 'X':
        print(f"Moved to already marked position {i+1}, {j}")
        return i+1, j
    elif data[i+1][j] == '#':
        is_down = False
        is_left = True
        print(f"Hit # at {i+1}, {j}")
        return i, j
    else:
        print(f"Unhandled case at {i+1}, {j}")
        return i, j

def move_left(i, j):
    global is_down, is_left, is_right, is_up, count
    if j - 1 < 0:
        print(f"Out of bounds moving left from ({i}, {j}). Final count: {count}")
        is_left = False
        return i, j
    elif data[i][j - 1] == '.':
        data[i][j - 1] = "X"
        count += 1        
        print(f"Moved left to {i}, {j-1}")
        return i, j - 1
    elif data[i][j - 1] == 'X':
        print(f"Moved to already marked position {i}, {j-1}")
        return i, j - 1
    elif data[i][j - 1] == '#':
        is_left = False
        is_up = True
        print(f"Hit # at {i}, {j-1}")
        return i, j
    else:
        print(f"Unhandled case at {i}, {j-1}")
        return i, j

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '^':
            data[i][j] = 'X'
            count += 1
            move(i, j)