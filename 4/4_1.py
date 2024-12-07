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
    if (i < 3 and j < 3):
        XMAS_2(i, j)
        XMAS_3(i, j)
        XMAS_4(i, j)

    if (i < 3 and j >= 3 and j < len(data[i]) - 3):
        XMAS_2(i, j)
        XMAS_3(i, j)
        XMAS_4(i, j)
        XMAS_5(i, j)
        XMAS_6(i, j)

    if (i < 3 and j >= len(data[i]) - 3):
        XMAS_4(i, j)
        XMAS_5(i, j)
        XMAS_6(i, j)

    if (i >= 3 and i < len(data) - 3 and j < 3):
        XMAS_0(i, j)
        XMAS_1(i, j)
        XMAS_2(i, j)
        XMAS_3(i, j)
        XMAS_4(i, j)

    if (i >= 3 and i < len(data) - 3 and j >= 3 and j < len(data[i]) - 3):
        XMAS_0(i, j)
        XMAS_1(i, j)
        XMAS_2(i, j)
        XMAS_3(i, j)
        XMAS_4(i, j)
        XMAS_5(i, j)
        XMAS_6(i, j)
        XMAS_7(i, j)

    if (i >= 3 and i < len(data) - 3 and j >= len(data[i]) - 3):
        XMAS_0(i, j)
        XMAS_4(i, j)
        XMAS_5(i, j)
        XMAS_6(i, j)
        XMAS_7(i, j)

    if (i >= len(data) - 3 and j < 3):
        XMAS_0(i, j)
        XMAS_1(i, j)
        XMAS_2(i, j)

    if (i >= len(data) - 3 and j >= 3 and j < len(data[i]) - 3):
        XMAS_0(i, j)
        XMAS_1(i, j)
        XMAS_2(i, j)
        XMAS_7(i, j)
        XMAS_6(i, j)

    if (i >= len(data) - 3 and j >= len(data[i]) - 3):
        XMAS_0(i, j)
        XMAS_7(i, j)
        XMAS_6(i, j)


def XMAS_0(i, j):
    global count
    if data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
        count += 1

def XMAS_1(i, j):
    global count
    if data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
        count += 1

def XMAS_2(i, j):
    global count
    if data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
        count += 1

def XMAS_3(i, j):
    global count
    if data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
        count += 1

def XMAS_4(i, j):
    global count
    if data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
        count += 1

def XMAS_5(i, j):
    global count
    if data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
        count += 1

def XMAS_6(i, j):
    global count
    if data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S":
        count += 1

def XMAS_7(i, j):
    global count
    if data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
        count += 1



for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            XMAS(i, j)

print(count)