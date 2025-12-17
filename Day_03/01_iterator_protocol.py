# The Infinite Input Pattern
while True:
    pwd=input('Enter a password (min 5 chars) :')
    if len(pwd)>=5:
        print('Password Set Successfully')
        break
    else :
        print('Password is too short. Try again.')