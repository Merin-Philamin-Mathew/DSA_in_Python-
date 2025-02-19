def count_down(n, message):
    while n>0:
        yield n
        n-=1
    yield message

message = 'Happy NewYear!'
for i in count_down(5,message):
    print(i)