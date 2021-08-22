class Student:
    clg = "Aligarh College of Engineering and Technology"

    def __init__(self, name, course, branch, rollno):
        self.nme = name
        self.crse = course
        self.brnch = branch
        self.rln = rollno
        self.special = "I am special"

    def prnt(self):
        print(f"The name is {self.nme} course is {self.crse} branch is {self.brnch} and roll no. is {self.rln} from {self.clg} ")

    @classmethod
    def strr(cls, string):
        # n = string.split("-")
        # return cls(n[0], n[1], n[2], n[3])
        return cls(*string.split("-"))


class Programmer(Student):
    def __init__(self, name, course, branch, rollno, language):
        super().__init__(name, course, branch, rollno)
        self.nme = name
        self.crse = course
        self.brnch = branch
        self.rln = rollno
        self.lng = language

    def prntcls(self):
        return f"The name is {self.nme} and branch is {self.brnch} with course {self.crse} and the languages are {self.lng}"


rohan = Student("Prateek Chaudhary", "Pharmacy", "B.Pharma", 24352245244)
sandy = Student("Sandeep Singh", "Btech", "CSE", 1901090100059)
ravi = Programmer("Ravi Teja", "BCA", "BBA", 345672345, ["Python", "C"])
print(ravi.prntcls())
print(ravi.special)
