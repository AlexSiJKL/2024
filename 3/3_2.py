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
pattern_not_to_do = r"don't\(\)"
pattern_to_do = r"do\(\)"

combined_pattern = f"{pattern}|{pattern_not_to_do}|{pattern_to_do}"

matches = re.findall(combined_pattern, data)

nums = []
skip = 0
for mul in matches:
    if "don't()" in mul:
        skip = 1
    elif "do()" in mul:
        skip = 0
    elif re.search(r'\d+', mul) and skip == 0:
        cleaned_match = mul[4:-1]
        num1, num2 = map(int, cleaned_match.split(','))
        nums.append((num1, num2))

sum = 0
for num in nums:
    sum += (num[0] * num[1])

print(sum)