a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if(a>b):
    if(a>c):
        print("Largest number is",a)
    else:
        print("Largest number is",c)
else:
    if(b>c):
        print("Largest Number is",b)
    else:
        print("Largest number is",c)
    
