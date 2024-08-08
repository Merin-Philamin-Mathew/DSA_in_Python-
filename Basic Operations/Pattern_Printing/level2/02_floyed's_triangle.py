# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

row = 5
k = 1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k += 1
    print()
