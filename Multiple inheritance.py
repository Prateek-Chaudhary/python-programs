class Student:
    clg = "Aligarh College of Engineering and Technology"

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


class Player:
    def __init__(self, name, game):
        self.name = name
        self.gme = game


class Pro(Student, Player):
    game = ["FootBall", "Cricket"]
    def gme(self):
        print(self.game)


rohan = Student("Prateek Chaudhary", "Pharmacy", "B.Pharma", 24352245244)
sandy = Student("Sandeep Singh", "Btech", "CSE", 1901090100059)
jazy = Pro("Jazzy", "HCL", "IT", 23456)
jazy.gme()
print(jazy.prnt())
