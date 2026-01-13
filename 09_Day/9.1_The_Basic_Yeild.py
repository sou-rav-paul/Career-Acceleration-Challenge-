# def gen():
#     yield 1
#     yield 2
#     yield 3
# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))

def gen():
    yield 1
    yield 2
    yield 3
    
genarator = gen()
for i in genarator:
    print(i)
