def fibonacci_with_gen(a , b):
    # print(f'{a}\n{b}')
    count=0
    while True:
        print(a)
        c = a + b
        a , b = b , c
        print(count)
        count +=1
        yield c

fibo = fibonacci_with_gen(0,1)

for _ in range(10):
    print(next(fibo))