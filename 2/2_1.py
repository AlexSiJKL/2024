import os.path

filename = "2.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

reports = []
count = 0

try:
    file = open(os.path.join(path, filename), "r")
    reports = [tuple(map(int, line.strip().split())) for line in file]
except Exception as e:
    print("Failed to create file for int:", e)
finally:
    file.close()

for levels in reports:
    d_safe = True
    inc_safe = True
    dec_safe = True

    for i in range(len(levels) - 1):
        
        if abs(levels[i] - levels[i + 1]) > 3:
                d_safe = False
        
        if levels[i] <= levels[i + 1]:
                inc_safe = False
        
        if levels[i] >= levels[i + 1]:
                dec_safe = False

    if d_safe and (inc_safe or dec_safe):
        count += 1

print(count)