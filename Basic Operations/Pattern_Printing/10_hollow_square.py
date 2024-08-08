# *****
# *   *
# *   *
# *   *
# *****
row = 5
for i in range(1,row+1):
    print("*"*row) if i == 1 or i == row else print("*"+" "*(row-2)+"*")
        

    