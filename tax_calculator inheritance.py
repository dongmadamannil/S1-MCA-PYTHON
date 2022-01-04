class Home:
    def __init__(self,area,loca):
        self.area=area
        self.loca=loca;
    def taxcal(self):
        if(self.loca=="co"):
            return (self.area*.50)+500
        else:
            return self.area*.50
            
class flat(Home):
    def __init__(self,area,loca):
        Home.__init__(self,area,loca)
    def taxcl(self):
        return self.taxcal()+self.taxcal()*0.05
s1=flat(500,"co")
print("Tax=",s1.taxcl())
s2=Home(500,"co")
print("Tax=",s2.taxcal())
#Multilevel inheritance with class having contructor       
