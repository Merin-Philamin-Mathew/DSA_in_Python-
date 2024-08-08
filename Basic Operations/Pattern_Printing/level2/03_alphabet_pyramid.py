#     A
#    A B
#   A B C
#  A B C D
# A B C D E

row = 5
k = 64
for i in range(1,row+1):
    print(" "*(row-i) + ''.join(chr(k+i)+" " for i in range(1,i+1)))