def slice_list(my_list,k):
    # Step 1: Allocate memory for k items 
    new_list = [0]*k
    
    # Step 2: Copy values one by one 
    for i in range(0,k):
        new_list[i] = my_list[i]   #Copy reference 
    
    return new_list


my_list = list(range(1000000))
sliced_list = slice_list(my_list,10)
print(sliced_list)