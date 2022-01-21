class Time:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __add__(self, o):
        return "Hour:"+str(self.a+o.a),"Minute:"+str(self.b+o.b),"Second:"+str(self.c+o.c)
print("Enter 1st time")
ob1 = Time(int(input("Hour ")),int(input("minute")),int(input("second.")))
print("Enter 2nd time")
ob2 = Time(int(input("Hour ")),int(input("minute")),int(input("second.")))
print(ob1 + ob2)
#After 60sec or 60 min

