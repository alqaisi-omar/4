# Получаем значение n от пользователя
n = int(input("Введите натуральное число n: "))

# Инициализируем переменную для хранения суммы факториалов
sum_of_factorials = 0

# Используем цикл for для вычисления суммы факториалов от 1 до n
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum_of_factorials += factorial

# Выводим результат
print(f"Сумма факториалов от 1 до {n} равна: {sum_of_factorials}")
