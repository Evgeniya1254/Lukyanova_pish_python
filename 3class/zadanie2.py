def cyclic_shift(matrix, shift):
    result = []
    for row in matrix:
        row_shifted = row[-shift:] + row[:-shift]
        result.append(row_shifted)
    return result

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
shift = 1

result = cyclic_shift(matrix, shift)
print(result)