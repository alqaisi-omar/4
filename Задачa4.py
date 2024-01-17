# Вводим количество чисел N
N = int(input("Введите количество чисел N: "))

# Инициализируем переменную для суммы
sum_numbers = 0

# Вводим N целых чисел и суммируем их
for _ in range(N):
    while True:
        try:
            num = int(input("Введите целое число: "))
            sum_numbers += num
            break
        except ValueError:
            print("Ошибка! Введите корректное целое число.")

# Выводим сумму
print("Сумма введенных чисел:", sum_numbers)
