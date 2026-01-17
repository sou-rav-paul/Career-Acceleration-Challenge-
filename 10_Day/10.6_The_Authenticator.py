USER = None
def auth_wrapper(func):
    def checking_func():
        if USER !='admin':
            raise PermissionError('Sorry! Only admin allowed.')
        return func()
    return checking_func

@auth_wrapper
def login_info(): 
    return 'Login Sucessfully.\n'
    
USER = 'sourav'
try: 
    print(login_info())
except PermissionError as p:
    print(p)

USER = 'admin'
print(login_info())
