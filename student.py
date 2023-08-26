class Student:
    def __init__(self, fn,ln) -> None:
        self.fname=fn
        self.lname=ln
    def GetFullNameEth(self):
        print("Your full name is   " + self.fname, self.lname)
    def GetFullName(self):
        print("Your full name is   " + self.lname, self.fname)
        
s1=Student("Samuel","Tamirat")
s2=Student("Yoseff","Kasaye")
s1.GetFullNameEth()
s2.GetFullName()

