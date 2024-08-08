#Find array elements that occur exactly three times
from collections import Counter

def elements_occuring_three_times(lst):
    # Count the occurrences of each element
    counts = Counter(lst)
    
    # Find the elements that occur exactly three times
    result = [elem for elem, count in counts.items() if count == 3]
    
    return result

lst = [3, 2, 4, 3, 5, 3, 2, 4, 5, 1]
print(elements_occuring_three_times(lst))
