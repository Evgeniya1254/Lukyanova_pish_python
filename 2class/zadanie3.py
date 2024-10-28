#верно ли, что в заданном числе сумма цифр равна их произведению
def check_sum_equals_product(number):
    digits = [int(digit) for digit in str(number)]
    
    digit_sum = sum(digits)
    digit_product = 1
    for digit in digits:
        digit_product *= digit
    
    return digit_sum == digit_product

number = int(input("Введите число: "))
if check_sum_equals_product(number):
    print("Сумма цифр равна произведению.")
else:
    print("Сумма цифр не равна произведению.")