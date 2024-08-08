def binarysearch(lst, l, r, x):
    while l<=r:
        mid = l + (r-l)//2
        if x == lst[mid]:
            return mid
        elif x>lst[mid]:
            l = mid+1
        else:
            r = mid-1
    return None

def binarySearch(lst, x, l, r):
    if l<=r:
        mid = l + (r-l)//2
        if x==lst[mid]:
            return mid
        elif x>lst[mid]:
            return binarySearch(lst, x, mid+1, r)
        else:
            return binarySearch(lst, x, l, mid-1)
    else:
        return None

lst = [1,2,3,4]
x = 4
result = binarysearch(lst, 0, len(lst)-1, x)
# result = binarySearch(lst,x, 0, len(lst)-1)

if result is not None:
    print(f"Element found at index {result}")
else:
    print("Element not found")