class Student: 
    def __init__(self, name, roll,curs): 
        self.name = name 
        self.roll = roll
        self.curs=curs
list = [] 
n=int(input("ENter limit"));
for i in range(n):
 print("Enter details of ",i,"th students")
 list.append( Student(input("ENter name "), input("ENter roll"),input("Enter course")) )
i=0;
print("\n\n\nDEtails of sudents\n\n");
for obj in list:
    i=i+1
    print("details of ",i,"Students\n");
    print( "name=",obj.name,"\nRoll no:" ,obj.roll,"\n Course:",obj.curs)
    print("\n\n\n");
