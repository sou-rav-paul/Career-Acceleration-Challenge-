def hash_lookup(target,set_obj):
    # Step 1: Compute mathematical signature
    hash_value=hash(target)
    # Step 2: Calculate memory address
    bucket_index = hash_value % set_obj.total_buckets

    # Step 3: Direct Jump
    memory_slot = set_obj[bucket_index]

    if memory_slot ==target:
        return True
    return False

import time

my_list=[0]*1000000
my_set=set(my_list)
list_time_start=time.time()
list_check=-5 in my_list
list_time_end=time.time()
list_time=list_time_end-list_time_start
print('Checking for list :')
print('Found? :',list_check,',  Total time: ',list_time*10000)

set_time_start=time.time()
set_check=-5 in my_set
set_time_end=time.time()
set_time=set_time_end-set_time_start
print('\nChecking for Set :')
print('Found? :',set_check,', Total time :',set_time*10000)

print(f'Set is {list_time//set_time}x faster' )