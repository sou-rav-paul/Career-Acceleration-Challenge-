import time

a = [i for i in range(10000)]
b = [i-9990 for i in range(10000)]
duplicate=[]
start = time.time()
for i in range(10000):
    for j in range(10000):
        if a[i]==b[j]:
            duplicate.append(a[i])
end_time=time.time() - start

print(f'For O(N^2) : {end_time}')
start=time.time()
duplicate1=[i for i in a if i in b]
end_time = time.time()-start
print(f'For O(N)   : {end_time}')

