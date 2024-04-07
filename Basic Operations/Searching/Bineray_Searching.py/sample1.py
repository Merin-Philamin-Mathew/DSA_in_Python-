def binarysearch(lst, l, r, x):
    while l<=r:
        mid = l + (r-l)//2

        if x == lst[mid]:
            return mid
        
        elif x>lst[mid]:
            l = mid+1
        
        else:
            r = mid-1

    return -1

lst = [1,2,3,4]
x = 2
result = binarysearch(lst, 0, len(lst)-1, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")