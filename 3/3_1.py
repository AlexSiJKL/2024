import os.path
import re


filename = "3.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

try:
    file = open(os.path.join(path, filename), "r")
    data = file.read()
except Exception as e:
    print("Failed to create file for int:", e)
finally:
    file.close()

pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(pattern, data)
nums = []

for mul in matches:
    cleaned_match = mul[4:-1]
    num1, num2 = map(int, cleaned_match.split(','))
    nums.append((num1, num2))

sum = 0
for num in nums:
    sum += (num[0] * num[1])

print(sum)