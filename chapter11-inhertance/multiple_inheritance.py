class Father:   # base class 1 
    def __init__(self, fatherfname , lname, father_haircolor):   # This is just a constructor of class Father
        self.fatherfname = fatherfname
        self.lname = lname
        self.father_haircolor = father_haircolor

    def showfatherfname(self):
        print(f"The first name of father is : {self.fatherfname}")
       
    def showlname(self):
        print(f"The last name is : {self.lname}")

    def showfather_haircolor(self):
        print(f"The hair color is : {self.father_haircolor}")

class Mother:   # base class 2               
    def __init__(self, mother_haircolor):    # this is just a constructor of class of Mother
        self.mother_haircolor = mother_haircolor

    def showmother_haircolor(self):     
        print(f"The hair color  is : {self.mother_haircolor}")

class Son(Father, Mother):
    def __init__(self, sonfname, fatherfname, lname, father_haircolor, mother_haircolor):
        Father.__init__(self, fatherfname, lname, father_haircolor)
        Mother.__init__(self, mother_haircolor)
        self.sonfname = sonfname
            
    def showsonfname(self):
        print(f"The first name of the Son is : {self.sonfname}")

# objects
f = Father("Bheshraj", "Chaudhary" ,"Dark black")
s = Son("Rajiv", "Bheshraj", "Chaudhary", "Dark black", "Light brown and black")
m = Mother("Light brown and black")

# calls
f.showfatherfname()
f.showlname()
f.showfather_haircolor()
print("\n")
m.showmother_haircolor()
print("\n")
s.showsonfname()
s.showlname()
s.showmother_haircolor()
