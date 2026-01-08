def build_dict_from_list(my_list):
    new_dict = {}
    
    for item in my_list:
        new_dict[item] = item 

    return new_dict

import time
my_list = list(range(10000000))
start_creation = time.time()
nw_dict = build_dict_from_list(my_list)
end_creation = time.time() - start_creation 
print(f'Buliding dict time : {end_creation:.8f} s')

start_search = time.time()
flag = -1 in nw_dict
end_search = time.time() - start_search

print(f'Searching dict time : {end_search:.8f} s')