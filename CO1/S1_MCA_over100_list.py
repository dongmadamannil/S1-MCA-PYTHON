lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    if(ele>100):
        ele="over"    
    lst.append(ele) 
     
print(lst)
