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

directions = {
    "up": True,
    "right": False,
    "down": False,
    "left": False
}

def move(i, j):
    global count, directions
    while directions["up"] or directions["down"] or directions["left"] or directions["right"]:
        if directions["down"]:
            i, j = move_down(i, j)
        elif directions["left"]:
            i, j = move_left(i, j)
        elif directions["right"]:
            i, j = move_right(i, j)
        elif directions["up"]:
            i, j = move_up(i, j)

    print(f"Final count: {count}")

def move_up(i, j):
    global directions, count
    if i - 1 < 0:  # Выход за верхнюю границу
        print(f"Out of bounds moving up from ({i}, {j}). Final count: {count}")
        directions = False
    elif data[i-1][j] == '.':
        data[i-1][j] = "X"
        count += 1
        print(f"Moved up to {i-1}, {j}")
        return i-1, j
    elif data[i-1][j] == 'X':
        print(f"Moved to already marked position {i-1}, {j}")
        return i-1, j
    elif data[i-1][j] == '#':
        directions["up"] = False
        directions["right"] = True
        print(f"Hit # at {i-1}, {j}")
        return i, j
    else:
        print(f"Unhandled case at {i-1}, {j}")
        return i, j
        
def move_down(i, j):
    global directions, count
    if i + 1 >= len(data):  # Выход за нижнюю границу
        print(f"Out of bounds moving down from ({i}, {j}). Final count: {count}")
        directions = False
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
        directions["down"] = False
        directions["left"] = True
        print(f"Hit # at {i+1}, {j}")
        return i, j
    else:
        print(f"Unhandled case at {i+1}, {j}")
        return i, j

def move_right(i, j):
    global directions, count
    if j + 1 >= len(data[i]):  # Выход за правую границу
        print(f"Out of bounds moving right from ({i}, {j}). Final count: {count}")
        directions = False
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
        directions["right"] = False
        directions["down"] = True
        print(f"Hit # at {i}, {j+1}")
        return i, j
    else:
        print(f"Unhandled case at {i}, {j+1}")
        return i, j

def move_left(i, j):
    global directions, count
    if j - 1 < 0:  # Выход за левую границу
        print(f"Out of bounds moving left from ({i}, {j}). Final count: {count}")
        directions = False
        return i, j
    elif data[i][j-1] == '.':
        data[i][j-1] = "X"
        count += 1        
        print(f"Moved left to {i}, {j-1}")
        return i, j-1
    elif data[i][j-1] == 'X':
        print(f"Moved to already marked position {i}, {j-1}")
        return i, j-1
    elif data[i][j-1] == '#':
        directions["left"] = False
        directions["up"] = True
        print(f"Hit # at {i}, {j-1}")
        return i, j
    else:
        print(f"Unhandled case at {i}, {j-1}")
        return i, j

# Поиск начальной позиции '^'
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '^':
            data[i][j] = '.'
            move(i, j)