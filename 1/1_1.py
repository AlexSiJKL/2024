import os.path

filename = "1.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

lines = []
left = []
right = []

try:
    file = open(os.path.join(path, filename), "r")
    lines = [line.strip() for line in file.readlines()]
except Exception as e:
    print("Failed to create file for int:", e)
finally:
    file.close()  # Close the file

for line in lines:
    parts = line.split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))

left.sort()
right.sort()

sum = 0

for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)