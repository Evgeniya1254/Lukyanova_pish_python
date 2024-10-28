def max_subarray(array, k):
    n = len(array)
    if n < k or k <= 0:
        return None

    max_sum = float('-inf')
    current_sum = sum(array[:k])
    max_subarray_start = 0

    for i in range(1, n - k + 1):
        current_sum = current_sum - array[i - 1] + array[i + k - 1]
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_subarray_start = i

    return array[max_subarray_start:max_subarray_start + k]

array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 3

result = max_subarray(array, k)
print(result) 
