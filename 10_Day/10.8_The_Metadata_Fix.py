from functools import wraps
def deco(func):
    @wraps(func)
    def wrap():
        print('A')
        return func()
    return wrap

@deco
def hello():
    print('Hello')

hello()
print(hello.__name__)