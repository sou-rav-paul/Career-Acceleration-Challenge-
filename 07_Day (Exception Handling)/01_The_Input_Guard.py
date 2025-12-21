
while True:
    try:
        age=int(input('Enter your age :'))
        print('Age :',age)
        break
    except ValueError:
        print('Text is not allowed.')
    