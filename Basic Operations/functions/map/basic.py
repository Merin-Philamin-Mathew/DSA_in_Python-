nums = [2,4,5,6,7]
# mappedNums = list(map(lambda x: -x,nums))
# print(mappedNums)

# mappedNums = list(map(str,nums))
# print(mappedNums)

# mappedNums = ' '.join(map(str,nums))
# print(mappedNums)

# mappedNums = ', '.join(map(str,nums))
# print(mappedNums)

# mappedNums = tuple(map(lambda x: 2*x, nums))
# print(mappedNums)

# TypeError: cannot convert dictionary update sequence element #0 to a sequence
mappedNums = dict(map(lambda x: 3*x, nums))
print(mappedNums)