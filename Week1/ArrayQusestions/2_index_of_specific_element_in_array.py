# def index_of_element(arr,data):
#     for i,num in enumerate(arr):
#         if num == data:
#             return i
    

# data = 4
# arr = [5,4,6,6,0,5]

# print(f"index of {data} is: {index_of_element(arr,data)}")
def index_of_element(arr,element):
    try:
        index = arr.index(element)
    except:
        index = -1
    return index

arr = [4,5,6,7,8,9]
element_to_find = int(input(f"Enter the element you want to find in the array,{arr}:"))
print(f"The index of {element_to_find} in {arr} is: {index_of_element(arr,element_to_find)}")