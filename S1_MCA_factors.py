x=int(input("ENter number"))
print("The factors of",x,"are:")
for i in range(1, x + 1):
       if x % i == 0:
           print(i)
        
