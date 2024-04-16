#Find the second largest element in the array without sorting (Assume no elements are repeating)
def second_largest(lst):
    l1=float('-inf')
    l2=float('-inf')
    for i in lst:
        if i>l1:
            l2 = l1
            l1 = i
        elif i>l2:
            l2 = i
    return l2

lst = [2,4,1,5,12,5,6,3]
print(second_largest(lst))