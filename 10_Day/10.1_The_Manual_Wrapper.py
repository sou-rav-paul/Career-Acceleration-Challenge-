def wrapper(func):
    print('Before the function.')
    func()
    print('After the function.')
    return wrapper

def old_func():
    print('Hello Kaka. Tumi kemon acho?')


new_func = wrapper(old_func)
new_func