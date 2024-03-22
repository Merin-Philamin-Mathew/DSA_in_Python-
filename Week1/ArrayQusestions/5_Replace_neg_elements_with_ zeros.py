def replace_negative(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=0
    return arr

arr = [4,-2,0,3,3-4,-2]
print(f"arr with zeros in negative places: {replace_negative(arr)}")