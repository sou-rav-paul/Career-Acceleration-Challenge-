def pop_from_start(my_list):
    target = my_list[0]
    n=len(my_list)
    # Start from 0 , pull everyone one step left
    for i in range(n-1):
        my_list[i]=my_list[i+1] # Shift Operation
    return target


import time
my_list=[0]*100000
first_pop_start=time.time()
val_first = my_list.pop(0)
first_pop = time.time() - first_pop_start

last_pop_start = time.time()
val_last = my_list.pop()
last_pop = time.time() - last_pop_start

print(f'Poping time for first value :{first_pop:.8f}')
print(f'Poping time for last  value :{last_pop:.8f}')
print(f'last pop takes {first_pop/last_pop}x less time ')