import os.path

# Укажите имя файла
filename = "9.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

# Пытаемся открыть файл и прочитать данные
try:
    with open(os.path.join(path, filename), "r") as file:
        data = file.read()
except Exception as e:
    print("Failed to create file for int:", e)
    data = ""  # Задаем пустую строку в случае ошибки

# Преобразуем символы в числа
numbers = [int(char) for char in data if char.isdigit()]

data_set = []
num = 0  # Инициализируем переменную num

# Начинаем формировать список списков
for i in range(len(numbers)):
    if i % 2 == 0:  # Четные индексы - числа
        if numbers[i] > 0:  # Проверяем, что количество больше 0
            num_list = [num for _ in range(numbers[i])]  # Создаем список из числа
            data_set.append(num_list)  # Добавляем список в data_set
            num += 1  # Увеличиваем num для следующей группы чисел
    else:  # Нечетные индексы - точки
        if numbers[i] > 0:  # Проверяем, что количество точек больше 0
            dot_list = ["." for _ in range(numbers[i])]  # Создаем список из точек
            data_set.append(dot_list)  # Добавляем список точек в data_set

for k in range(len(data_set) - 1, -1, -1):
    if (len(data_set[k]) > 0):
        if isinstance(data_set[k][0], (int)):
            for j in range(0, k):
                if (len(data_set[j]) > 0):
                    if data_set[j][0] == '.':
                        def_j_k = len(data_set[j]) - len(data_set[k])
                        if def_j_k >= 0:
                            num_move = data_set.pop(k)
                            data_set.insert(j, num_move)
                            lnj = len(data_set[j])
                            del data_set[j + 1][def_j_k:]
                            if lnj > 0:
                                dots_move = ['.'] * lnj
                                data_set.insert(k+1, dots_move)
                            break


data_set = [nums for nums in data_set if nums]

data_set = [item for sublist in data_set for item in sublist]

print(data_set)

check_sum = 0


for x in range(0, len(data_set)):
    if isinstance(data_set[x], (int)):
        check_sum += data_set[x] * x

print(check_sum)