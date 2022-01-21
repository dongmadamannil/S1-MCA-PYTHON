class Rectangle:
    def __init__(self, a,b):
        self.length = a
        self.width=b
    def __lt__(self, o):
        if((self.length*self.width)<(o.length*o.width)):
            return "Area of Rectangle1 is lessthan Area of Rectangle2"
        else:
            return "Area of Rectangle2 is lessthan Area of Rectangle1"

ob1 = Rectangle(int(input("Enter length of 1st rectangle ")),int(input("Enter width of 1st rectangle")))
ob2 = Rectangle(int(input("Enter length of 2nd rectangle ")),int(input("Enter width of 2nd rectangle")))
print(ob1 < ob2)


