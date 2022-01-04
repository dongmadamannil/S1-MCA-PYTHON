class Student:
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name;
        self.course=course;
    def display(self):
        print("roll_no:",self.roll)
        print("Name:",self.name)
        print("course:",self.course)
class Test(Student):
    def __init__(self,roll,name,course,mrk):
        Student.__init__(self,roll,name,course)
        self.mark=mrk
    def disto(self):
        self.display()
        print("Mark=",self.mark);
s1=Test(115,"Don","MCA",100)
s1.disto()
#inheritance with class having contructor       
