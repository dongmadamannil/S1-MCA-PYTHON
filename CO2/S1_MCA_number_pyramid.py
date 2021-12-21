x=int(input("Enter limit"))
for i in range(x+1):
    j=0
    c=1
    while(c<=i):
        j=j+i
        print(j,"\t",end="")
        c=c+1
    print()
