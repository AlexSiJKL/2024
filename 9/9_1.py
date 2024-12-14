import os.path


filename = "9.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

try:
    file = open(os.path.join(path, filename), "r")
    data = file.read()
except Exception as e:
    print("Failed to create file for int:", e)
finally:
    file.close()

numbers = [int(char) for char in data]

data_set = []
num = 0

for i in range(0,len(numbers)):
    if i % 2 == 0:
        for j in range (numbers[i]):
            data_set.append(num)
        num += 1
    if i % 2 != 0:
        for j in range (numbers[i]):
            data_set.append(".")

for k in range(len(data_set) - 1, -1, -1):
        if "." in data_set[:k]:
            data_set[data_set.index(".")] = data_set[k]
            data_set[k] = "."
        else:
            print("Done")

check_sum = 0

for x in range(0, len(data_set)):
    if isinstance(data_set[x], (int)):
        check_sum += data_set[x] * x

print(check_sum)