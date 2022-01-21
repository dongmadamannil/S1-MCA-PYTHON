class A:
    def __init__(self, a,b):
        self.a = a
        self.b=b
 
    def salcal(self):
        self.m= self.a * self.b
    def __lt__(self, o):
        if(self.m<o.m):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is lessthan ob1"


ob1 = A(int(input("Enter working days of 1st employee ")),int(input("Enter daily salary of 1st employee ")))
ob1.salcal()
ob2 = A(int(input("Enter working days of 2nd employee ")),int(input("Enter daily salary of 2nd employee ")))
ob2.salcal()

print(ob1 < ob2)


