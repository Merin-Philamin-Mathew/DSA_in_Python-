def infinite_seq():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_seq():
    print(i)