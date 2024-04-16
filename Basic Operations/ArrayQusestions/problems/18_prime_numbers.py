#Find prime numbers in an array
def prime_number(lst):
    prime_numbers = []
    for i in lst:
        if i <= 1:  # Skip numbers less than or equal to 1
            continue
        is_prime = True
        for j in range(2,i//2+1):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers
lst = [1,2,3,4,5,6,7,8]
print(prime_number(lst))