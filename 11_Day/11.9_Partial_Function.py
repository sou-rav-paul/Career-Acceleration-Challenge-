item = [(1,2),(3,4)]
def change_tuple(tuple_item):
    try: 
        tuple_item[0]+=10
    except TypeError as e:
        return str(e)

modified_tuple = list(map(change_tuple,item))
print(modified_tuple)