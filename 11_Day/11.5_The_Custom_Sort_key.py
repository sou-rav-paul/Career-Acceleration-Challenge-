pixel_list = ['100px','20px','3px']

# sorted() function takes positional argument follows keyword argument
sorted_list = sorted(pixel_list, key = lambda x:int(x[:-2]))
print(sorted_list)

# Output: ['3px','20px','100px']

