def Check_value(target,my_list):
    index=0
    length=len(my_list)
    while index< length:
        current_val=my_list[index]
        if current_val==target:
            return True
        index+=1
    return False


my_list=[0]*1000000

print(Check_value(-5,my_list))
