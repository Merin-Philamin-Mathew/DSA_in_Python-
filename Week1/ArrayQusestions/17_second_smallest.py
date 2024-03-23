#Find the second smallest element in the array without sorting (Assume no elements are repeating)
def second_smallest(lst):
    s1=float('inf')
    s2=float('inf')
    for i in lst:
        if i<s1:
            s2 = s1
            s1 = i
        elif i<s2:
            s2 = i
    return s2

lst = [2,4,1,5,12,5,6,3]
print(second_smallest(lst))