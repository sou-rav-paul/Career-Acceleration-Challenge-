def divide_two_number(a,b):
    try:
        print(f'Result {a}/{b} :',a/b)
    except ZeroDivisionError:
        print(f'Not possible to divide  {a}/{b}')
    finally:
        print('Excution Complete.')
print('\nDivision without error in Below :\n')
divide_two_number(10,20)
print('\nHandling Error in Below :\n')
divide_two_number(10,0)