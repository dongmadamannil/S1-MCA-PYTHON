class Student:
    def getd(self,roll,name,course):
        self.roll=roll
        self.name=name;
        self.course=course;
    def display(self):
        print("roll_no:",self.roll)
        print("Name:",self.name)
        print("course:",self.course)
class Test(Student):
    def getmark(self,mrk):
        self.mark=mrk
    def disto(self):
        self.display()
        print("Mark=",self.mark);
s1=Test()
s1.getd(115,"Don","MCA")
s1.getmark(100)
s1.disto()
#inheritance       
