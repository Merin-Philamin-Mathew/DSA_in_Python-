# 4 3 2 1
# 4 3 2 
# 4 3 
# 4 

rows = 4

for i in range(rows+1):
    for j in range(rows, i, -1):
        print(j, end=' ')
    print()