def sample_generator():
    yield 1
    yield 2
    yield 3

gen = sample_generator()

try:
    while True:
        print(next(gen))
except StopIteration:
    pass