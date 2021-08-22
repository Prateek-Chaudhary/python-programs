d1={"harry":"12th","shyam":"11th","mohan":"10th","prateek":"btech","pratik":"BSc"}
print(type(d1))
#print(d1)
print(d1.keys())
print(d1.items())
print(d1["harry"],d1["pratik"])
d1.update({"rohan":"5th"})
d2=d1.copy()
#print(d1)
print(d2)
del d1["mohan"]
print(d1)