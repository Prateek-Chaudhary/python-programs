class Student:
    clg = "Aligarh College of Engineering and Technology"
    _protect = 109
    __private = 1801800800

    def __init__(self, name, course, branch, rollno):
        self.nme = name
        self.crse = course
        self.brnch = branch
        self.rln = rollno

    def prnt(self):
        print(f"The name is {self.nme} course is {self.crse} branch is {self.brnch} and roll no. is {self.rln} from {self.clg} ")

    @classmethod
    def strr(cls, string):
        # n = string.split("-")
        # return cls(n[0], n[1], n[2], n[3])
        return cls(*string.split("-"))

    @staticmethod
    def stat(ss):
        print(f"this is a {ss}")


rohan = Student("Prateek Chaudhary", "Pharmacy", "B.Pharma", 24352245244)
sandy = Student("Sandeep Singh", "Btech", "CSE", 1901090100059)
jimmy = Student("Jammy", "MCA", "CC", 5435345363)
ranjan = Student.strr("Ranjan singh-Bachelor-BBA-345676")
# rohan.name = "Rohan Singh"
# rohan.course = "Btech"
# rohan.branch = "CSE"
# rohan.rollno = 1901090100049
print(sandy.clg)
print(rohan.nme)
print(jimmy.rln)
Student.prnt(rohan)
print(ranjan.crse)
ranjan.stat("ascvht43456ygfdsdfghj")
print(sandy._protect)
print(sandy._Student__private)
