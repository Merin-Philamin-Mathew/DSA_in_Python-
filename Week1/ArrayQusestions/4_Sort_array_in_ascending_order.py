def ascending_order(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

arr = [4,5,3,6,1,7,0]
print(f"ascending order of {arr} is {ascending_order(arr)}")
print(f"sorted(arr),{sorted(arr)}")
arr.sort()
print(f"arr.sort(),{arr}")
print(f"arr.sort(),{arr.sort()}")