class Wallet:
    def __init__(self,tk):
        self.balance = tk
    
    def __add__(self,other):
        total = self.balance + other.balance
        return Wallet(total)
    
    def __str__(self):
        return f'Total balance is : {self.balance}'

w1 = Wallet(100)
w2 = Wallet(20)
w = w1 + w2
print(w)
print(w1)
print(w2)