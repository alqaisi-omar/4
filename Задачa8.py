# Получаем значение n от пользователя
n = int(input("Введите натуральное число n (n ≤ 9): "))

# Проверяем, что n не превышает 9
if n > 9:
    print("Ошибка: n должно быть не больше 9.")
else:
    # Используем цикл for для генерации лесенки
    for i in range(1, n + 1):
        # Формируем строку для текущей ступеньки
        stair = ''.join(str(j) for j in range(1, i + 1))
        # Выводим текущую ступеньку
        print(stair)
