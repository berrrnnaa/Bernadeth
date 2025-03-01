class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def describe(self):
        print(f"Book Details: '{self.title}' by {self.author}, published in {self.year_published}")

# Creating book objects
book1 = Book("Girl Last Seen", "Nina Laurin", 2017)
book2 = Book("Lines Between Us", "MsKindGirl", 2019)
book3 = Book("Mafia Boss", "Khardine Gray", 2019)

# Displaying book details
book1.describe()
book2.describe()
book3.describe()
