class Student:

    def __init__(self, name, course, branch):
        self.name = name
        self.crse = course
        self.branch = branch

    @classmethod
    def str_dash(cls, string):
        # ns = string.split("-")
        # return cls(ns[0], ns[1], ns[2])
        return cls(*string.split("-"))

    @staticmethod
    def staticthis(strr):
        print("This is a tutorial for this" + strr)


Prateek = Student("Prateek", "Btech", "CSE")
Sandeep = Student("Sandeep", "BCA", "CA")
karan = Student.str_dash("Karan-Pharmacy-D.Pharma")
print(Prateek.crse)
print(Sandeep.branch)
print(Prateek.__dict__)
print(karan.branch)
Sandeep.staticthis("dfknegff")
