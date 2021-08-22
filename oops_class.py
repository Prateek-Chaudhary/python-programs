class Employee:
    no_of_leaves = 45

    def printself(self):
        return f"Name is {self.name} and salary is {self.sal}"

    @classmethod
    def leaves(cls, leaves):
        cls.no_of_leaves = leaves


harry = Employee()
rohan = Employee()
harry.name = "Harry"
harry.sal = 435434
rohan.name = "Rohan"
rohan.sal = 43000
print(Employee.__dict__)
print(harry.__dict__)
rohan.leaves(34)
print(rohan.printself())
print(Employee.no_of_leaves)
