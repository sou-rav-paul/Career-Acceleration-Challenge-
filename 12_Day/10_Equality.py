class User:
    def __init__(self,num):
        self.number = num
    
    def __eq__(self,other):
        return self.number == other.number
    

user1 = User(1)
user2 = User(1)
print(user1==user2)