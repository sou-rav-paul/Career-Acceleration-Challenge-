def custom_signal():
    while True:
        num=int(input('Enter a number :'))
        try:
            if num<0:
                raise ValueError ('This is negative ')
            return num
        except ValueError as err:
            print(f'Error : {err}')
result=custom_signal()
print('Final result :',result)