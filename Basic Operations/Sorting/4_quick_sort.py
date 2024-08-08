print("================QUICK SORT=================")

def quickSort(array,left,right):
    #when left goes beyond right
    #when i moves more left side than j
    #if condition fails and no sorting happens
    if left<right:
        partition_pos = partition(array,left,right)
        quickSort(array,left,partition_pos-1)
        quickSort(array,partition_pos+1,right)

def partition(array,left,right):
    i = left
    j = right-1
    pivot = array[right]

    while i<j:
        while i<right and array[i] < pivot:
            print("1",array)
            i+=1
        while j>left and array[j] > pivot:
            print("2",array)
            j-=1
        print("3",array)
        if i < j:
            array[i],array[j] = array[j],array[i]
            print('4',array)
    #i>j
    #left and right positions meets
    if array[i]>pivot:
        array[i],array[right] = array[right],array[i]
    return i

array = [44,33,55,3,6,88,4,6,1,20]

quickSort(array, 0, len(array)-1)
print(array)

