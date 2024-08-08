#     *
#    * *
#   *   *
#  *     *
# *********
# 123456789

row = 5

for i in range(1,row+1):
    for j in range(1,2*row):
        if j-i == row-1 or i == row or j+i == row+1 :
            print("*",end="")
        else:
            print(" ", end="")
    print()