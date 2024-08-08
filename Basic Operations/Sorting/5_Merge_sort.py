print("================MERGE SORT=================")


def mergeSort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        print(left_arr)
        print(right_arr)
        mergeSort(left_arr)
        print("d")
        mergeSort(right_arr)

        i = 0
        j = 0
        k = 0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1

# arr = [300,50,20,10,13,8,5,4,3]
# arr =  [6,43,7,4,7,4,5,6,34,1]
arr = [1,6,5,4,5,3,2,1]

print("unsorted list:", arr)
mergeSort(arr)
print("sorted arrayf:", arr)


            
