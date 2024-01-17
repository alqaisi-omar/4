A = int(input("Введите значение A: "))
B = int(input("Введите значение B: "))

if A < B:
    # Вывод чисел от A до B включительно в порядке возрастания
    for num in range(A, B + 1):
        print(num, end=" ")
else:
    # Вывод чисел от A до B включительно в порядке убывания
    for num in range(A, B - 1, -1):
        print(num, end=" ")
