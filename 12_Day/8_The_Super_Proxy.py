class Base:
    def __init__(self):
        print("1. Base - end")
class Base1:
    def __init__(self):
        print('8. Base1 - start')
        super().__init__()
        print('10. Base1 - end')

class ParentA(Base1,Base):
    def __init__(self):
        print("2. ParentA-start")
        super().__init__() 
        print("3. ParentA-end")

class ParentB(Base1, Base):
    def __init__(self):
        print("4. ParentB-start")
        super().__init__() 
        print("5. ParentB-end")

class Child(ParentA, ParentB):
    def __init__(self):
        print("6. Child-start")
        super().__init__() 
        print("7. Child-end")

# অবজেক্ট তৈরি
obj = Child()