print("================SELECTION SORT=================")

# arr = [300,50,20,10,13,8,5,4,3]
arr =  [6,43,7,4,7,4,5,6,34,1]
print("unsorted list:", arr)

for i in range(len(arr)-1):
    small_index = i
    print(i,small_index)    #for analysis and study purpose only not a relevant line of code
    for j in range(i+1,len(arr)):
        if arr[small_index] > arr[j]:
            print(arr[small_index] ,">", arr[j])  #
            small_index = j
            print(small_index)  #
    arr[i],arr[small_index] = arr[small_index],arr[i]
    print(arr,end="")  # 
    print()  # 
print("sorted array:", arr)