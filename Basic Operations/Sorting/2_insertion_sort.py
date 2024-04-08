print("================INSERTION SORT=================")
arr = [300,50,20,16,13,8,5,4,3,80]
arr =  [6,43,7,4,7,4,5,6,34,1]
n = len(arr)
for i in range(1,n):
    curr = arr[i]
    prev = i - 1
    print(i,"/",prev)
    while prev >= 0 and arr[prev]>curr:
        arr[prev+1] = arr[prev]
        print(arr,"*")
        prev-=1
    arr[prev+1]=curr
    print()
    print(arr,end="")
    print()

print("sorted array:", arr)