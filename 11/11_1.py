import os.path

# Open and read the input file
filename = "11.txt"
current_directory = os.path.dirname(os.path.abspath(__file__))
path = current_directory

data = []

# Читаем данные из файла и преобразуем в список целых чисел
with open(os.path.join(path, filename), "r") as file:
    data = list(map(int, file.read().split()))

def Blink(data, passes):
    for _ in range(passes):  # Повторяем обработку списка `passes` раз
        blinked_data = []
        for num in data:
            if num == 0:
                blinked_data.append(1)
            elif len(str(num)) % 2 == 0:  # Проверяем, что количество цифр чётное
                num_str = str(num)  # Преобразуем число в строку
                mid = len(num_str) // 2  # Определяем середину
                blinked_data.append(int(num_str[:mid]))  # Левая часть
                blinked_data.append(int(num_str[mid:]))  # Правая часть
            else:
                blinked_data.append(num * 2024)  # Если нечётное количество цифр, умножаем на 2024
        data = blinked_data  # Обновляем список для следующего прохода
    return blinked_data

# Вызываем функцию
passes = 35  # Задаём количество проходов
blinked_data = Blink(data, passes)
print(len(blinked_data))
