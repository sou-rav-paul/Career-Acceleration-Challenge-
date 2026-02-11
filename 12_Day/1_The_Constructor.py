class User:
    def __init__(self,username):
        self.name = username
        self.is_active = True

user_obj = User('sourav')
print(user_obj.name,user_obj.is_active)