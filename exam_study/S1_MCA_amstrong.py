def amstro(x):
    n=int(x)
    ams=int(0)
    while(x!=0):
        d=int(x%10)
        ams=int(ams+d*d*d)
        x=int(x/10)
    if(ams==n):
        print("Anstrong")
    else:
        print("Not Amstrong")
amstro(int(input("Enter Number")))
