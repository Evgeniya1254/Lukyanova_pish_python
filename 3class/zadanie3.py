def reverse_blocks(array, block_size):
    for i in range(0, len(array), block_size):
        block = array[i:i+block_size]
        array[i:i+block_size] = block[::-1]
    return array

array = [1,2,3,4,5,6,7]
block_size = 3
output = reverse_blocks(array, block_size)
print(output)