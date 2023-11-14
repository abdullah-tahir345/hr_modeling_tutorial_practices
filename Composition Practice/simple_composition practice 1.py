class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        
class Book:
    def __init__(self, title, genre, author):
        self.title = title
        self.genre = genre
        self.author = author
        
    def display_info(self):
        print(f'Title : {self.title}')
        print(f'Genre : {self.genre}')
        print(f'Author Name : {self.author.name}')
        print(f'Author Nationality : {self.author.nationality}')
        
author_book1 = Author('Jane Auston', 'American')
book_1 = Book('End of the World', 'Drama', author=author_book1)
book_1.display_info()