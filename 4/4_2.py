import os.path

filename = "4.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

try:
    file = open(os.path.join(path, filename), "r")
    data = file.read().splitlines() 
except Exception as e:
    print("Failed to create file for int:", e)
finally:
    file.close()

count = 0

def XMAS(i, j):
    global count
    if (data[i - 1][j - 1] == "M") and (data[i + 1][j - 1] == "S" and (data[i + 1][j + 1] == "S" and (data[i - 1][j + 1] == "M"))):
        count += 1
    if (data[i - 1][j - 1] == "M") and (data[i + 1][j - 1] == "M" and (data[i + 1][j + 1] == "S" and (data[i - 1][j + 1] == "S"))):
        count += 1
    if (data[i - 1][j - 1] == "S") and (data[i + 1][j - 1] == "M" and (data[i + 1][j + 1] == "M" and (data[i - 1][j + 1] == "S"))):
        count += 1
    if (data[i - 1][j - 1] == "S") and (data[i + 1][j - 1] == "S" and (data[i + 1][j + 1] == "M" and (data[i - 1][j + 1] == "M"))):
        count += 1

for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if data[i][j] == "A":
            XMAS(i, j)

print(count)