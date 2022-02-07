file_obj = open("file1.txt","r")
fk=open("test_d.txt","w")  
line_list = []
line_list = file_obj.readlines()
print("The Existing file\n\n")
for m in line_list:
    print(m)
print("\n\n***********************************\n");
for k in line_list:
    l=k.split()
    z=l[0]
    if(len(l)>5 and z[0].isupper()):
        fk.write(k)
fk.close()
fk1=open("test_d.txt","r")  
print("\n\nNew File \n \n")
line_list1 = fk1.readlines()
for j in line_list1:
          print(j)

