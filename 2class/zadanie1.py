def formula(x):
    if -2 <= x < 2:
        result = x * x
    elif x >= 2:
        result = x * x + 4 * x + 5
    else: 
        result = 4
    
    return int(result) 
2
x = float(input("Введите значение x: "))
output = formula(x)
print("Результат:", output)