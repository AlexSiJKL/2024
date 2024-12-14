import os.path

filename = "10.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

try:
    with open(os.path.join(path, filename), "r") as file:
        data = [[int(char) for char in line] for line in file.read().splitlines()]
except Exception as e:
    print("Failed to create file for int:", e)

rows = len(data)
cols = len(data[0])

extended_data = [[-1] + row + [-1] for row in data]

extended_data.insert(0, [-1] * (cols + 2))
extended_data.append([-1] * (cols + 2))

visited = set()

def Pathfinder(value, i, j):
    global visited
    if value == 9 and (i , j) not in visited:
        visited.add((i, j))
        return
    if extended_data[i - 1][j] == value + 1:
        Pathfinder(value + 1, i - 1, j)
    if extended_data[i][j + 1] == value + 1:
        Pathfinder(value + 1, i, j + 1)
    if extended_data[i + 1][j] == value + 1:
        Pathfinder(value + 1, i + 1, j)
    if extended_data[i][j - 1] == value + 1:
        Pathfinder(value + 1, i, j - 1)

count = 0

for i in range (1, len(extended_data) - 1):
    for j in range(1, len(extended_data[i]) - 1):
        if extended_data[i][j] == 0:
            visited.clear()
            Pathfinder(0, i, j)
            count += len(visited)

print(count)