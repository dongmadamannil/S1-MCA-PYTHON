a=input("Enter string")
b=int(input("Enter the position of letter to remove"))
a1=a[0:b-1]
a2=a[b:]
print(a1+a2)