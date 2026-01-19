import time 
# Squred element with map() function
map_start = time.time()
map_squared = list(map(lambda x:x*x,list(range(1000000))))
print(f'Mapping time : {time.time()-map_start} ms')

# Squred element with comprehension 
comprehension_start = time.time()
comprehen_squred = [i*i for i in range(1000000)]
print(f'Comprehension time :{time.time()-comprehension_start} ms')