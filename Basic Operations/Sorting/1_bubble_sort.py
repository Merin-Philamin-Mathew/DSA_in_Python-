print("================BUBBLE SORT=================")

arr = [300,50,20,16,13,8,5,4,3]
print("unsorted list:", arr)
for j in range(len(arr)-1):
    print(j)
    for i in range(len(arr)-1): #or for i in range(len(arr)-j-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        #     print(arr, end="*")
        # else:
        #     print(arr, end="")

        # print()
print("sorted list is", arr)
