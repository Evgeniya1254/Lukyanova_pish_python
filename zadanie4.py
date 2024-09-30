def check(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if int(num_str[i]) > int(num_str[i + 1]):
            return False
    return True

input_number = int(input("Введите целое число: "))
if check(input_number):
    print("Все цифры числа расположены в порядке возрастания.")
else:
    print("Не все цифры числа расположены в порядке возрастания.")