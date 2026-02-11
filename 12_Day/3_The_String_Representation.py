class Book:
    def __init__(self,id,title):
        self.id = id
        self.title = title
    def __str__(self):   # Without this , instance will print just a memory address
        return f'This is class of books {self.title}'
    def __repr__(self):  # for end user to let know how to use this
        return 'Book(id = 100, title = \'code\')'
    
book1 = Book(101,'Bangla')
print(book1)
print(repr(book1))
print(f'ID is : {book1.id}')
print(f'Title is : {book1.title}')