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

l=[]
n=int(input("Enter number of students"))
print("Enter details of ",n," Students")
for i in range(n):
    print("Enter details of ",len(l)," Student")
    l.append(Test1(input("Enter roll_no"),input("Enter Name"),input("Enter course"),input("Enter Mark"),input("Enter Hostl status"))) 
print("\n\n\n\n")
for i in l:
    i.displyall()
    print("\n\n")
    
#Multilevel inheritance with class having contructor       
