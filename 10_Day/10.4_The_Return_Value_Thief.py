def decorator(func):
    def wrapper():
        print('Hello')
        func()
        print('The end')
        
@decorator
def outer_fun():
    print('This this outer function.')


print(outer_fun) 