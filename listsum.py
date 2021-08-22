ls = [10, 20, "yes", "30", 10.0]
s = 0
for i in ls:
    j = str(i)
    if j.isalpha():
        continue
    else:
        s = s + float(j)
print(s)
