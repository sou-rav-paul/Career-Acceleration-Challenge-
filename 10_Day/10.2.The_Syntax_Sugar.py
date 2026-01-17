def decorator(func):
    def wrapper():
        print('Before function')
        func()
        print('After function.')
        # return 'Kollapatu'
    return wrapper
@decorator
def say_hello():
    print('Hello')

value = say_hello()
print(value)