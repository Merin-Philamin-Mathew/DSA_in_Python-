import functools
nums = [1,2,3,4]
# Syntax --> reduce(func, iterable[, initial])

doubled = list(map(lambda x:x*2 , nums))
product = functools.reduce(lambda x,y: x*y , nums)
product_half = functools.reduce(lambda x,y: x*y , nums, 0.5) 
sum = functools.reduce(lambda x,y: x+y , nums)

print(doubled)
print(product)
print(product_half)
print(int(product_half))
print(sum)