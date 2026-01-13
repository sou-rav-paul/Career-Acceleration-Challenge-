import sys 
my_list = [x for x in range(10000000)]
my_gen = (x for x in range( 10000000))
print(f'Memory for list : {sys.getsizeof(my_list)} byte')
print(f'Memory for generator : {sys.getsizeof(my_gen)} byte')