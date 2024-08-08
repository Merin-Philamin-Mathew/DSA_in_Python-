#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

row = 5
for i in range(1,row+1):
    print(" "*(row-i) + ''.join(str(i)+" " for i in range(1,i+1)))