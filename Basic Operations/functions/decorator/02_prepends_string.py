def prepend_decorator(prepend_str):
    def decorator(func):
        def wrapper():
            # Call the original function
            original_result = func()
            # Prepend the specified string to the result
            return prepend_str + original_result
        return wrapper
    return decorator

@prepend_decorator("Prepended: ")
def say_hello():
    return "Hello, world!"

# Call the function
result = say_hello()
print(result)

print('===================ADJECTIVE DECORATOR=======================')
# if fn to be decorating have arguments wrapper fn should receive those
def adjective_decorator(prepend_str):
    def decorator(func):
        def wrapper(*args):
            return prepend_str + func(*args)
        return wrapper
    return decorator

@adjective_decorator('smart ')
def name(name):
    return name

print(name('merin'))
