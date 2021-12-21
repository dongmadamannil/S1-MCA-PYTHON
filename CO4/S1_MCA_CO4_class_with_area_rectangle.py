class Rectangle:
    def __init__(self,val1,val2):
        self.length=int(val1)
        self.breadth=int(val2)
    def area(self):
        return self.length*self.breadth
    def perim(self):
        return 2*(self.length+self.breadth)
r1=Rectangle(input("Enter length of 1st rectangle"),input("Enter breadth of 1st rectangle"))
r2=Rectangle(input("Enter length of 2nd rectangle"),input("Enter breadth of 2nd rectangle"))       

if(r1.area()>r2.area()):
    print("area of 1st is larger")
else:
    print("area of 2nd rectangle is larger")
