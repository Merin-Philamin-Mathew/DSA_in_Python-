def average_even(arr):
    sum = 0
    c = 0
    for num in arr:
        if num % 2 == 0:
            sum += num 
            c += 1
   
    if c > 0:
        average = sum/c
        return f"average of even elements in {arr} is {average}"
    else:
        return f"There are no even elements in {arr} "

arr = [9,8,7,61]
print(average_even(arr))