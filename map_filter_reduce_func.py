from functools import reduce
import math

lst = [1, 2, 3, 4, 5]
a = list(map(lambda x:x*x, lst))
print(a)

lst2 = [2, 4, 6, 8, 10, 3, 5, 76,4, 67, 75645, 23, 46, 779, 24, 72, 3, 57, 243]
b = list(filter(lambda y:y>10, lst2))
print(b)

lst3 = [2, 4, 6, 8, 10]
c = reduce(lambda p, q:p+q, lst3)
print(c)
