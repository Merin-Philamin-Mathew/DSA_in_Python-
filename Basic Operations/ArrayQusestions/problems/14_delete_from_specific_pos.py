def delete_elem(lst,pos):
    for i in range(pos,len(lst)-1):
        lst[i] = lst[i+1] 
    lst.pop()
    return lst


lst = [2,1,3,5,3,6]
position = 1
print(lst)
print(delete_elem(lst,position))
