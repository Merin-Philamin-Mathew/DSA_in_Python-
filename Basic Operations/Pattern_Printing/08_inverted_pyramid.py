# ******* 7
#  *****  5
#   ***   3
#    *    1

row = 4

for i in range(row,0,-1):
    n = 2*i - 1
    print(" "*(row-i) + "*"*n)