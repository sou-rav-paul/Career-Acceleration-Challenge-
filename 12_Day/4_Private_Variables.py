class User:
    def __init__(self,name,age,password):
        self.name = name
        self.age = age
        self.__password = password   # Name Mangling as _User__password
    

user1 = User('Sourav',24,'sour12rav')
print('Name :',user1.name)
print('Password :',user1._User__password)

print(user1.__dict__)