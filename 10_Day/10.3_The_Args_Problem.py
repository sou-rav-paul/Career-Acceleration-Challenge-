def decorator(func):
    def wrapper(*args):
        print('The Summation :',func(*args))
    
    return wrapper
      
@decorator
def add(a,b):
    return a+b
add(2,3)