from datetime import datetime

class User :
    def __init__(self,name,birth_year,password):
        self.name = name 
        self.__birth_year = birth_year
        self.__password = password
    @property
    def age(self):
        current_year = datetime.now().year
        return current_year - self.__birth_year
    @age.setter
    def age(self,year):
        self.__birth_year = datetime.now().year - year
        




user1 = User('Sourav',2002,'sour2002av')
fake = user1.age
print(fake)
user1.age = 30
print(user1.age)

