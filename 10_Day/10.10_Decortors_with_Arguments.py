def repeat(times):
    def deco(func): 
        def wrap(*args):
            for _ in range(times):
                print(f'For {_} : {args}')
                a,b,c=func(*args)
                args=(a,b,c)
                
        return wrap
    return deco
@repeat(3)
def print_func(*args):
    a,b,c=args
    a+=1
    b+=1
    c+=1
    return a,b,c  
print_func(1,2,3)