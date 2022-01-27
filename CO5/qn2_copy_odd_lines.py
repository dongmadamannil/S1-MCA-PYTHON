f=open("D:\PROGRAMMING\lab mca\S1-MCA-PYTHON\S1_MCA_amstrong.py","r")
fk=open("test_d.txt","w")  
line_list = f.readlines()
for j in range(0,len(line_list)):
    if(j%2==0):#0th item is 1st line ,so consider even items as odd line 
          fk.write(line_list[j])
fk.close()
#bellow printing
print("\n\n****initial file****\n\n")
for j in line_list:
    print(j)
new_fk=open("test_d.txt","r")
print("\n\n****new file****\n\n\n")
for j in new_fk.readlines():
    print(j)
f.close()
new_fk.close();

