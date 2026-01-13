def gen():
    count = 0
    total_value = 0
    while True:
        x = yield f'Taking value for {count}'
        total_value+=x
        count+=1
        print(f'Total value {total_value} for {count} iteration')

generator_obj = gen()
next(generator_obj)

my_list = [10,20,30]
for x in my_list:
    print(generator_obj.send(x))
