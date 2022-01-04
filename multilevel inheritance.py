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

class Test1(Test):
    def __init__(self,roll,name,course,mrk,hostel_flg):
        Test.__init__(self,roll,name,course,mrk)
        self.hstl=hostel_flg
    def displyall(self):
        self.disto()
        print("Hostel=",self.hstl);
s1=Test1(115,"Don","MCA",100,"false")
s1.displyall()
#Multilevel inheritance with class having contructor       
