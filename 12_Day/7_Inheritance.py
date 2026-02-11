class User:
    def __init__(self,user_pass):
        self.__user_pass = user_pass
    def hei_kaka(self):
        print('Hei,Kaka')
class User1:
    def __init__(self,password):
        self.__user_pass = password
class Admin(User,User1):                      # take 'User' class as MRO(Msthod of Resolution Order)
    def __init__(self,name,age,password):
        super().__init__(password)
        self.name = name
        self.age = age
    
    def delete_db(self):
        pass

admin1 = Admin('sourav',25,'sou12rav')

print('Name : ',admin1.name)                  # sourav
print('Age : ',admin1.age)                    # 25
print('Password : ',admin1._User__user_pass)  # sou12rav

 
