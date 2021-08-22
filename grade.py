print("Enter the subject marks out of 100\n")
e = int(input("Enter the marks for english\n"))
h = int(input("Enter the hindi marks\n"))
m = int(input("Enter the maths marks\n"))
p = int(input("Enter the physics marks\n"))
c = int(input("Enter the chemistry marks\n"))
tm = e + h + m + p + c
print("Total marks = ", tm)
per = tm/5
print("Percentage = ", per)
if per > 90:
    print("Grade A")
elif per > 80 and per < 90 :
    print("Grade B")
elif per > 70 and per < 80 :
    print("Grade C")
elif per > 60 and per < 70 :
    print("Grade D")
else:
    print("Fail")
