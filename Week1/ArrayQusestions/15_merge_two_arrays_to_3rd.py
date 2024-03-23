def two_arrays(arr1,arr2):
    #method1
    # arr3 = []
    # arr3 = arr1+arr2 
    
    #method2
    arr3 = arr1
    arr3.extend(arr2)
    return arr3

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]
print(two_arrays(arr1,arr2))