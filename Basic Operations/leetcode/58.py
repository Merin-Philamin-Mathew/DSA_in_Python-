string = "   There are many problems in everyones life   "
list1 = list(string.split(" "))
print(list1)
for i in range(len(list1)-1,-1,-1):
    if list1[i] != " ":
        print(list1[i]," ",len(str(list1[i])))

print([0]*3)
