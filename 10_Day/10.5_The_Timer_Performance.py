import time
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'Total time taken :{(end - start):20.18f}')
        return result
    return wrapper
@timer
def summation(a,b):
    return a+b
value = summation(2,4)
print(f"The total value : {value}")