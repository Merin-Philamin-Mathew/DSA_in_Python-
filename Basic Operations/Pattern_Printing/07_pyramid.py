#    *       1 3
#   ***      3 2
#  *****     5 1
# *******    7

row = 4
for i in range(1,row+1):
    n = 2*i-1
    print(" "*(row-i) + "*"*n)