# Получаем количество чисел Фибоначчи от пользователя
N = int(input("Введите количество чисел Фибоначчи: "))

# Инициализируем первые два элемента ряда
fibonacci_sequence = [0, 1]

# Генерируем остальные элементы ряда
for i in range(2, N):
    next_fibonacci = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_fibonacci)

# Выводим сгенерированный ряд Фибоначчи
print("Ряд Фибоначчи:", fibonacci_sequence)

# Считаем и выводим сумму чисел Фибоначчи
sum_fibonacci = sum(fibonacci_sequence)
print("Сумма чисел Фибоначчи:", sum_fibonacci)
