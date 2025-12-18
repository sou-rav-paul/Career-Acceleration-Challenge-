# Creating a empty list 
data=[]
data.append(1)
data.append(2)
data.append(3)

print('Actual list :',data)
# pop() function delete the last element and return that 
popped_element=data.pop()
print('List after poping :',data)
print('Removed Element :',popped_element)