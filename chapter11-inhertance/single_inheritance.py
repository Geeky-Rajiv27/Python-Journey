class father:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def showfname(self):
        print(f"The first name of the father is: {self.fname}")

    def showlname(self):
        print(f"The last name is: {self.lname}")

class Son(father):
    def __init__(self, sfname, lname):
        # Call the constructor of the parent class (father)
        super().__init__(sfname, lname)
        
    def sonfname(self):
        print(f"The first name of the Son is: {self.sfname}")

# Create instances
f = father("Bheshraj", "Chaudhary")
s = Son("Rajiv", "Chaudhary")

# Call methods for the father object
f.showfname()
f.showlname()

# Call methods for the son object
s.sonfname()
s.showlname()




