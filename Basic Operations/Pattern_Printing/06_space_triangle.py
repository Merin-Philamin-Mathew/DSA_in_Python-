          # 
        # #
      # # #
    # # # #
#   1 2 3 4

rows =4

for i in range(rows+1):
    for j in range(rows+1):
        if j+i >= rows+1:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()