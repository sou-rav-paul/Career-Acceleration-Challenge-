from functools import reduce

reduce_obj = reduce(lambda a,b:a*b,list(range(1,6)))
print(reduce_obj)

# Input: [1,2,3,4,5]
# Output: 120
