def fun(n):
    if(n<=1):
        return 
    fun(n-1)
    print(n,end="")
    fun(n-1)

fun(5)