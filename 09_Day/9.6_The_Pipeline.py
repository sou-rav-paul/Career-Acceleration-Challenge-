def squares(nums):
    for x in nums:
        yield x*x

def filters(numbers):
    for x in numbers:
        if x%2==0:
            yield x

my_list = [i for i in range(20)]
flag = filters((squares(my_list)))
for i in flag: 
    print(i)

