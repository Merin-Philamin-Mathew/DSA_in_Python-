def average_odd_elements(lst,sum=0,c=0):
    if not lst:
        if c>0:
            return sum/c
        else:
            return 0 
    else:
        if lst[0]%2:
            sum += lst[0]
            c += 1
        return average_odd_elements(lst[1:],sum,c)

lst = [2,4,1,1,1,6]
print(f"Average of odd elems:{average_odd_elements(lst)}")