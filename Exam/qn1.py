import csv 
dict_value = [
{"name":"binoy","MFC":56,"DC":99,"DS":100,"ASE":94},
{"name":"Gokul","MFC":66,"DC":59,"DS":56,"ASE":74},
{"name":"Arun","MFC":66,"DC":59,"DS":12,"ASE":94},
{"name":"Mohith","MFC":56,"DC":99,"DS":90,"ASE":64},
{"name":"Melvin","MFC":56,"DC":99,"DS":100,"ASE":94},
{"name":"Nidhin","MFC":46,"DC":99,"DS":60,"ASE":94},
{"name":"Riya","MFC":36,"DC":99,"DS":56,"ASE":23},
{"name":"Merin","MFC":96,"DC":99,"DS":100,"ASE":96},
{"name":"Ancy","MFC":56,"DC":99,"DS":95,"ASE":94},
{"name":"Neethi","MFC":26,"DC":99,"DS":66,"ASE":94},]

fields = ["name","MFC","DC","DS","ASE"]

with open('student.csv','w') as c:
    writer = csv.DictWriter(c,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    c.close()
mfc=0
dc=0
ase=0
ds=0
with open('student.csv','r') as cfiles:
     reader = csv.DictReader(cfiles)
     for row in reader:
         print(row['name'],":",(int(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/400)*100)
         mfc=mfc+int(row['MFC'])
         dc=dc+int(row['DC'])
         ase=ase+int(row['ASE'])
         ds=ds+int(row['DS'])
print("\n\nAverage of subjcts")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)



