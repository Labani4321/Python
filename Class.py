class Book :
    def __init__(self,title,author,year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def print_details(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"year published:{self.year_published}")
        print ("you are a car")
book = Book("The girl with no name","Marina Chapman", 2013)
book.print_details()




