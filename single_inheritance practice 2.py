# Hierarchical Inheritance : When multiple derived classes are created
# from one base class then this is called hierarchical inheritance.

# Parent/Base Class
class Book(object):
    def __init__(self, title, author, price):
        # Initialize attributes for a book
        self.title = title
        self.author = author
        self.price = price
        
    def display_info(self):
        # Display basic information about a book
        print(f"Book Title : {self.title}\nAuthor : {self.author}\nPrice : {self.price}")
        
# Derived Class
class EBook(Book):
    def __init__(self, title, author, price, book_format):
        # Call the constructor of the parent class (Book)
        super().__init__(title, author, price)
        # Additional attribute specific to eBooks
        self.book_format = book_format
        
    def display_info(self):
        # Call the display_info method of the parent class (Book)
        super().display_info()
        # Display additional information about an eBook
        print(f"Book Format : {self.book_format}")
        
# Derived Class
class PaperBook(Book):
    def __init__(self, title, author, price, weight):
        # Call the constructor of the parent class (Book)
        super().__init__(title, author, price)
        # Additional attribute specific to paper books
        self.weight = weight
        
    def display_info(self):
        # Call the display_info method of the parent class (Book)
        super().display_info()
        # Display additional information about a paper book
        print(f"Book Weight : {self.weight}")

# Instances of the classes
book1 = Book('Harry Potter In Hogwarts', 'James Gun', 1500)
book1.display_info()
print()
book2 = Book('End of the World', 'Julia Ann', 500)
book2.display_info()
print()
book3 = Book('Searching the Peace', 'Mark', 2000)
book3.display_info()

print('--------------------')

ebook1 = EBook('End of the World', 'Julia Ann', 500, 'PDF')
ebook1.display_info()

print('--------------------')

pb1 = PaperBook('Searching the Peace', 'Mark', 2000, '20KG')
pb1.display_info()
