def g():
    my_list = [1,2,3,4]
    for i in my_list:
        yield i
gen = g()
for value in gen:
    print(value)

print('This Loop print nothing .')
for value_again in gen:
    print(value_again)