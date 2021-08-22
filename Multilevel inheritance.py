class ElectronicGadgets:
    device = ["Phone", "TV", "Fridge", "Oven", "Fan"]


class PocketGadgets(ElectronicGadgets):
    pdevice = ["Phone", "Smart Watch", "Calculator"]

    def prntpdevice(self):
        return f"The pocket devices are {self.pdevice}"


class Phone(PocketGadgets):
    cmp = ["Apple", "One+", "Samsung"]

    def prntpdevice(self):
        return f"The pocket Phone i use " \
               f"is the company of {self.cmp}"


eg = ElectronicGadgets()
pg = PocketGadgets()
p = Phone()
print(p.prntpdevice())
print(pg.prntpdevice())
print(p.device)
