def inserting_elem(lst,pos,elem):
    lst.insert(pos, elem)
    # lst.append(0)
    # for i in range(len(lst)-1,pos,-1):
    #     lst[i] = lst[i-1] 
    # lst[pos]=elem
    return lst


lst = [2,1,3,5,3,6]
position = 4
element = ""
print(lst)
print(inserting_elem(lst,position,element))