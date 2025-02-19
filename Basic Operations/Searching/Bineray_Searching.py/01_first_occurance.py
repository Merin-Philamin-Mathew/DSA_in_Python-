def firstOccurence(list, left, right, elem):
    result  = None
    if left<=right:
        mid = left + (right-left)//2
        if elem == list[mid]:
            result = mid
            return firstOccurence(list, left, mid-1, elem) or result
        elif elem < list[mid]:
            return firstOccurence(list, left, mid-1, elem)
        else:
            return firstOccurence(list, mid+1, right, elem)
    return result

def firstOccurence(list, left,right, elem):
    result = None
    while left <= right:
        mid = left + (right-left)//2
        if elem == list[mid]:
            result = mid
            right = mid-1
        elif elem < list[mid]:
            right = mid-1
        else:
            left = mid+1
    return result

list = [3,4,4,4,5]
print(firstOccurence(list,0,len(list)-1,4))
