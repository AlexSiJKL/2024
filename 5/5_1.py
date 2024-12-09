import os.path

filename = "5.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

try:
    with open(os.path.join(path, filename), "r") as file:
        data = [list(line) for line in file.read().splitlines()]
except Exception as e:
    print("Failed to create file for int:", e)

print(data)