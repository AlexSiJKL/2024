import os.path

filename = "2.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

reports = []
reports_for_demp = []
count = 0

def safe(levels):
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

    return d_safe and (inc_safe or dec_safe)
    

try:
    file = open(os.path.join(path, filename), "r")
    reports = [tuple(map(int, line.strip().split())) for line in file]
except Exception as e:
    print("Failed to create file for int:", e)
finally:
    file.close()

for levels in reports:
    if safe(levels):
        count += 1
    else:
        reports_for_demp.append(levels)

print(count)

for levels in reports_for_demp:
    for i in range(len(levels)):
        modified_list = levels[:i] + levels[i+1:]
        if safe(modified_list):
            count += 1
            break

print(count)