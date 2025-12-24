# def insert_at_zero(my_list,new_value):
#     n=len(my_list)
    # Start from the end, move everyone one step right
    # for i in range(n,1,-1):
    #     my_list[i]=my_list[i-1] # The Shift Operation
    # Now index 0 is 'empty'(overwrite)
    # my_list[0]=new_value

import time



my_list = [0]*10000



append_time_start = time.time()
my_list.append(20)
append_time =  time.time() - append_time_start
# append_time = append_time_start

insert_time_start = time.time()
my_list.insert(0,20)
insert_time = time.time() - insert_time_start
# insert_time = insert_time_end - insert_time_start

print('Time for append 0(1):',append_time*1000)
print('Time for insert 0(N):',insert_time*1000)
print(f'Here , append operation is {insert_time/append_time}x less than insert operation.')