def gen():
    yield from [1,2,3]

g = gen()

try: 
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    print('There is stopiteration.')
    