len([1,2,3])
len('asdasd')
print([1,2,3])

class Book():


    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self): #string representation of the object when printed

        return "Title: {}, Author: {}".format(self.title, self.author)

    def __len__(self): #length of our object
        return self.pages

my_book = Book("Harry Potter", "JK Rowling", 750)
print(my_book)
length_book = len(my_book)
print(length_book)
