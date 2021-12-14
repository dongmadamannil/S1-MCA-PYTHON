class Student: 
    def __init__(self, name, roll,mark1,mark2,mark3): 
        self.name = name 
        self.roll = roll
        self.m1=mark1
        self.m2=mark2
        self.m3=mark3
list = [] 
n=int(input("ENter limit"));
for i in range(n):
 print("Enter details of ",i,"th students")
 list.append( Student(input("ENter name "), input("ENter roll"),int(input("ENter mark 1")),int(input("ENter mark 2")),int(input("ENter mark 3"))) )
print("\n\n\nDEtails of sudents\n\n");
for obj in list:
    print("details of ",i,"Students\n");
    print( "name=",obj.name,"\nRoll no:" ,obj.roll,"\n Percentge:",((obj.m1+obj.m2+obj.m3)/int(300))*int(100),"%")
    print("\n\n\n");
