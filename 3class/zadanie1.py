#сдвиг на заданное число позиций
array = [1, 2, 3, 4, 5]
shift = 2

array_shift = array[-shift:] + array[:-shift]

print(array_shift)