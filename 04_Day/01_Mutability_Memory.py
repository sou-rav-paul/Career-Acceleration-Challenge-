data=[10,20,30,40,50]
# Slicing (Start : Stop : Step)
subset=data[1:4]        # [20,30,40]
reverse=data[::-1]      # [50, 40, 30, 20, 10]

# List Comprehension
# [Action for Item in List if Conditions]

squares=[x*x for x in data]
print(squares)