def linearsearch(lst,elem,index=0):
    if index >= len(lst):
        return -1
    elif lst[index] == elem:
        return index
    else:
        return linearsearch(lst,elem,index+1)
    
# def linearsearch(lst,elem):
#     for i in range(len(lst)):
#         if lst[i] == elem:
#             return i
#     return -1
    
        
lst=[]
limit=int(input("Enter a limit: "))
for i in range(limit):
    if i<limit-1:
        values=int(input(f"Enter value{i+1}: "))
    else:
        values=int(input(f"Enter last value: "))
    lst.append(values)
print(lst)
element=int(input("Enter the value for search: "))

result = linearsearch(lst,element)

if result == -1:
    print("Element not found")
else:
    print(f"Element found at {result}")

