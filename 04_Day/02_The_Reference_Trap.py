# Effect of without copy() functions
a=[1,2,3]
b=a
b[0]=99
print('a',a)
print('b',b)
# Using copy() function 
a=a=[1,2,3]
b=a.copy()
b[0]=99
print('a', a)
print('b',b)