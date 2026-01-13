def sub_gen1():
    yield 1.1
    yield 1.2
def sub_gen2():
    yield 2.1
    yield 2.2


def main_gen():
    yield from sub_gen1()
    yield from sub_gen2()



object_main_gen = main_gen()

for i in object_main_gen:     # Output : 1.1 1.2 2.1 2.2 
    print(i)
    
    