def fac(n):
    if (n<=1):
        return 1 #ividunnan answer vidunnath instead 1 reccursion work ayyitt 120 than vidunnath
    else:
        return n*fac(n-1)

result=fac(4)
print(f"factorial of number is :{result}")