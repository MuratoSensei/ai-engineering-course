class Book:
    def __init__(self, title, author, release_year, pages):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.__pages = pages
    
    def get_pages(self):
        return self.__pages
    
    def __str__(self)
        return f"'{self.title}' by {self.author} ({self.release_year}) - {self.__pages} pages"
    
class AudioBook(Book):
    def __init__(self, title, author, release_year, duration):
        super().__init__(title, author, release_year, pages=0)
        self.duration = duration

    def __str__(self):
        return f"[AudioBook: '{self.title}' by {self.author} ({self.release_year}) - Duration:{self.duration} min]"