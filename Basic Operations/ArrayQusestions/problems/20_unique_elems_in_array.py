#Find unique elements in an array
def unique_elm(lst):
    unique_elems = set()
    for i in lst:
        unique_elems.add(i)
    return unique_elems
lst = [3,2,4,3,5,3,2,4,5,1]
print(unique_elm(lst))