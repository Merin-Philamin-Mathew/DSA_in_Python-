#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

rows1 = 9
rows = (rows1+1)//2
for i in range(1,rows):
    n = 2*i - 1
    print(" "*(rows-i) + "*"*n)
for i in range(rows,0,-1):
    n = 2*i -1
    print(" "*(rows-i) + "*"*n)
