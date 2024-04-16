def average_odd_elements(lst,sum=0,c=0):
    for i in lst:
        if i%2:
            sum += i
            c+=1
    if sum:
        return sum/c
    return 0

lst = [2,4,1,1,1,6]
print(f"Average of odd elems:{average_odd_elements(lst)}")