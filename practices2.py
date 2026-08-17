
class Publication():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @property
    def author(self) -> str: 
        return self._author
    
    @author.setter
    def author(self, author: str):
        if isinstance(author, str) == False:
            raise TypeError("Error: Author must be a string.")
        self._author = author
    
    @property
    def year(self): 
        return self._year

    @year.setter
    def year(self, year:int): 
        if isinstance(year, int) == False: 
            raise TypeError("Error: Year must be a integer")
        elif year<0: 
            raise ValueError("Error: Year must be more than 0")
        self._year = year

    def get_info(self): 
        return f'"{self.title}" ({self.author}, {self.year})'

class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def get_info(self):
        return f'{super().get_info()}, ISBN: {self.isbn}' 

class Magazine(Publication):
    def __init__(self, title, editor, year, issue_number): 
        super().__init__(title, editor, year)
        self.editor = editor
        self.issue_number = issue_number

    def get_info(self):
        return f'"{self.title}" (Ред. {self.editor}, {self.year}), Выпуск №{self.issue_number}' 







    