def argskwargs(nm, *lst, **kwargs):
    print(nm)
    for names in lst:
        print(names)
    for i, j in kwargs.items():
        print(i, j)
    

nm = "It is a normal string for args and kwargs"
ls = ["Name1", "Name2", "Name3", "Name4", "Name5"]
kw = {"N1": "Nubbile", "Ph": "Phone number", "Ro": "Roll number", "Sb": "Subject"}
argskwargs(nm, *ls, **kw)
