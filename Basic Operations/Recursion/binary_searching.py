def binarysearch(lst, l, r, x):
    if l <= r:
        mid = l + (r-l)//2

        if lst[mid] == x:
            return mid
        
        elif x > lst[mid]:
            return binarysearch(lst,mid+1,r,x)
        
        else:
            return binarysearch(lst,l,mid-1,x)
        
    return -1

lst = []
limit = int(input("Enter a limit: "))
for i in range(limit):
    lst.append(int(input(f"Enter value{i+1}: ")))
print(lst)
x = int(input("Enter the element you want to search: "))
result = binarysearch(lst, 0, len(lst)-1, x)

if result != -1:
    print(f"Element is found at index {result}")
else:
    print("Element is not found")
