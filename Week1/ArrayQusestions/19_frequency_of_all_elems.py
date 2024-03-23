#Find the frequency of all elements in the array.
def finding_frequency(lst):
    frequencies = {}
    for i in lst:
        if i in frequencies:
            frequencies[i] +=1
        else:
            frequencies[i] =1
    return frequencies
lst = [3,2,4,3,5,3,2,4,5,1]
print(finding_frequency(lst))