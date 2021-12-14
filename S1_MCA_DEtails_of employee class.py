class Emplyee: 
    def __init__(self, name,emid,salary,dept): 
        self.name = name 
        self.empid = emid
        self.salary=salary
        self.dept=dept
list = [] 
n=int(input("ENter Number of employes"));
for i in range(n):
 print("\n\nEnter details of ",i,"th Employee")
 list.append( Emplyee(input("ENter name "), input("ENter Eid"),int(input("Enter salary")),input("Enter department")) )
i=0;
print("\n\n\nDEtails of employees annual salary >50k\n\n");
for obj in list:
    if(int(obj.salary)==50000):
        i=i+1
        print("details of ",i,"employee\n");
        print( "name=",obj.name,"\nEmployee id:" ,obj.empid,"\n SALARY:",obj.salary,"\n DEPARTMENT:",obj.dept)
        print("\n\n\n");
