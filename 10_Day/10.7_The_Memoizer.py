def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n]= func(n) 
            print(f'{n}\'th fibo number is {cache[n]}')  
        
        return cache[n]
    return wrapper
@memoize
def fibo(n):
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)

print('Fibonacci of 5:\n')
fibo(12)
