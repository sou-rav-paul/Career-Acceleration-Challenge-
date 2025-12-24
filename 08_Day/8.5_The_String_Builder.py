def add_char(old_string):
    old_size = length(old_string)
    new_size = old_size + 1
    # Step 1: Allocate NEW Memory block
    new_memory = malloc(new_size)
    # Step 2: Copy ALL characters from old to new
    for i in range(old_size):
        new_memory[i]=old_string[i]
    # Step 3: Add the new character 
    new_memory[old_size] = char 
    return new_memory

import time
old_string='s'*100000
new_string=''
start= time.time()
for i in range(len(old_string)):
    new_string+=old_string[i]
# print('old: ',old_string)
# print('new: ',new_string)
copy_time = time.time() - start
print('Copying time 0(N^2):',copy_time)

start = time.time()
best_string = ''.join(old_string)
join_time = time.time() - start
print('Join time   0(N)   :',join_time)