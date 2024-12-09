from itertools import product

# Функция для перебора всех вариантов выражений с + и *
def generate_expressions(input_string):
    # Разделяем строку на числа
    numbers = input_string.split(", ")
    
    # Генерируем все комбинации операторов для (количество чисел - 1)
    operators = ['+', '*']
    combinations = product(operators, repeat=len(numbers) - 1)
    
    results = []  # Список для хранения выражений и результатов
    # Перебираем все комбинации операторов
    for combo in combinations:
        # Собираем выражение
        expression = "".join(f"{numbers[i]}{combo[i]}" for i in range(len(combo))) + numbers[-1]
        # Вычисляем результат
        result = eval(expression)
        results.append((expression, result))
    
    return results

# Пример использования
input_string = "9, 7, 18, 13"  # Можно заменить на любую строку с числами
expressions = generate_expressions(input_string)

# Печатаем все выражения и их результаты
for expr, res in expressions:
    print(f"{expr} = {res}")
