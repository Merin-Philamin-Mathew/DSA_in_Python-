def my_decorator(func):
    def wrapper():
        print('before function call')
        func()
        print('after function call')
    return wrapper

@my_decorator
def say_hello():
    print('hello')

say_hello()