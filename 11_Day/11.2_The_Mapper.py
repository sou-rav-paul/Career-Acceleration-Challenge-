# Creating map object using map() function
map_obj = map(lambda x:x**2,list(range(6)))

# Convert map object to list element
squred_list = list(map_obj)

print(squred_list) # Output: [0,1,4,9,16,25]