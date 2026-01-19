# Creating filter object using filter() function
filter_obj = filter(lambda x: x>=0,range(-5,5))
print(list(filter_obj))

# Input: [-5,-4,-3,-2,-1,0,1,2,3,4]
# Outpu: [0,1,2,3,4]
