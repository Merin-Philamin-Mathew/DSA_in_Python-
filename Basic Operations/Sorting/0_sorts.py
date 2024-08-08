arr = [300,50,20,16,13,8,5,4,3]
print("unsorted list:", arr)

# print("================BUBBLE SORT=================")
# for j in range(len(arr)-1):
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]

# print("================SELECTION SORT=================")
# for i in range(len(arr)-1):
#     small_index = i
#     for j in range(i+1,len(arr)):
#         if arr[small_index]>arr[j]:
#             small_index = j
#     arr[i],arr[small_index]=arr[small_index],arr[i]

# print("================INSERTION SORT=================")
# n =len(arr)
# for i in range(1,n):
#     curr = arr[i]
#     prev = i-1
#     while prev>=0 and arr[prev]>curr:
#         arr[prev+1] = arr[prev]
#         prev -= 1
#     arr[prev+1] = curr


# print("================QUICK SORT=================")
# def quickSort(array, left, right):
#     if left<right:
#         partition_pos = partition(array, left, right)
#         quickSort(array, left, partition_pos-1)
#         quickSort(array,partition_pos+1,right)

# def partition(array, left, right):
#     i = left
#     j = right
#     pivot = array[right]

#     while i<j:
#         while i<right and array[i]<pivot:
#             i+=1
#         while j>left and array[j]>pivot:
#             j-=1
#         if i<j:
#             array[i],array[j]=array[j],array[i]
#     if array[i]>pivot:
#         array[i],array[pivot] = array[pivot],array[i]
#     return i

# quickSort(arr, 0, len(arr)-1)
    
# print("================MERGE SORT=================")
# def mergeSort(arr):
#     if len(arr)>1:
#         # 1-->>>Divide: 
#         # Divide the unsorted list into n sublists,each containing one element 
#         # (a list of one element is considered sorted).
#         mid = len(arr) // 2
#         left_arr = arr[:mid]
#         right_arr = arr[mid:]
#         mergeSort(left_arr)
#         mergeSort(right_arr)

#         # 2--->Conquer:
#         #  Repeatedly merge sublists to produce new sorted sublists 
#         # until there is only one sublist remaining. This will be the sorted list.
#         i=0
#         j=0
#         k=0
#         while i<len(left_arr) and j<len(right_arr):
#             if left_arr[i]<right_arr[j]:
#                 arr[k]=left_arr[i]
#                 i+=1
#             else: 
#                 arr[k]=right_arr[j]
#                 j+=1
#             k+=1
#         while i<len(left_arr):
#             arr[k]=left_arr[i]
#             i+=1
#             k+=1
#         while j<len(right_arr):
#             arr[k]=right_arr[j]
#             j+=1
#             k+=1

# mergeSort(arr)
print("sorted list:", arr)

