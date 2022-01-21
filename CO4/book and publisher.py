class Publisher:
    def __init__(self,name):
        self.name=name;
    def display(self):
        print("Publisher:",self.name)
class Book(Publisher):
    def __init__(self,name,title,auther):
        Publisher.__init__(self,name)
        self.title=title
        self.auther=auther
    def display(self):
        Publisher.display(self)
        print("Title:",self.title);
        print("Auther:",self.auther);
class Python(Book):
    def __init__(self,name,title,auther,price,pages):
        Book.__init__(self,name,title,auther)
        self.price=price
        self.pages=pages
    def display(self):
        Book.display(self)
        print("Price:",self.price);
        print("Pages:",self.pages);
s1=Python("DC BOOKS","AARACHAR","MEERA",500,600)
s1.display()
#co4 last qn
