f = open("new.txt", "r+")
c = f.read()
lst = list(c)
s = str()
for i in lst:
    if i == "a" or i == "e" or i == "i":
        lst.remove(i)
for j in lst:
    s += str(j)
s = "\n" + s
f.write(s)
f.close()
