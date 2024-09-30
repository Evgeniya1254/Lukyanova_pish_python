a = int(input("Введите целое число a (0 <= a <= 100): "))
while a < 0 or a > 100:
    a = int(input("Введите целое число a (0 <= a <= 100): "))

b = int(input("Введите целое число b (0 <= b <= 100): "))
while b < 0 or b > 100:
    b = int(input("Введите целое число b (0 <= b <= 100): "))

if a > b:
    print("Ошибка: a должно быть меньше или равно b")
else:
    result = 0
    for i in range(a, b+1):
        result += i*i

    print("Сумма квадратов от", a, "до", b, "равна", result)
