def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# result = calculate_sum({1,2,3,4})
lst = [1,2,3,4,5]
result = calculate_sum(lst)
print("The sum of elements in the array is:",result)