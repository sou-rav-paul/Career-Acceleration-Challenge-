class Car :
    speed = 0
    def drive(self):
        self.speed = 100

my_car = Car()
print(my_car.drive())
print(my_car.speed)


class User:
    def name(self):
        self.age = 10

user1 = User()