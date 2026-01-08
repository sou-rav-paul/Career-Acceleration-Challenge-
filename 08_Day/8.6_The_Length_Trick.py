# STRUCT PyListObject:
#     int ob_size   # A generic integer variable
#     ptr *items    # Pointer to the actual data array
# FUNCTION get_length(list_obj):
#     # Does NOT loo. Just reads the variable 
#     RETURN list_obj.ob_size

my_list = list(range(10000000))


import time 
start = time.time()
length = len(my_list)
end_time = time.time() - start 
print(f'Total time needed : {end_time*10000}')
print(f'Gives the length instantly.')