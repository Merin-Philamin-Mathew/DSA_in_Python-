def array_in_reverse(arr):
    return arr[::-1]

def function(lst):
    n = len(lst)
    for i in range(n//2):
        j = n-1 -i
        lst[i],lst[j] = lst[j],lst[i]
        
    return lst

arr = [7,5,3,2,1]
print(f"arr {arr} in reverse is: {array_in_reverse(arr)}")
print(f"arr {arr} in reverse is: {function(arr)}")