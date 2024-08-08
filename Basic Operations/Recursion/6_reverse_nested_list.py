arr = [[1, 2], [3, [4, 5]], 6]
#     [6, [[5, 4], 3], [2, 1]]




def rev_list(arr):
    n = len(arr)-1
    if n<1:
        return arr
    rev = []
    while n>=0:
        if isinstance(arr[n], list):
            rev.append(rev_list(arr[n]))
            n-=1
        else:
            rev.append(arr[n])
            n-=1
    return rev


print('list')
result = rev_list(arr)
print('rev',result)



def reverse_nested_list(input_list):
    if isinstance(input_list, list):
        return [reverse_nested_list(item) for item in reversed(input_list)]
    else:
        return input_list

input_list = [[1, 2], [3, [4, 5]], 6]
output_list = reverse_nested_list(input_list)
print(output_list)
