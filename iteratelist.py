list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
list3 = [6, 8, 3, 9, 1, "abc", "xyz", "dff", "oik", "ert"]
for i, j, k in zip(list1, list2, list3):
    print(i)
    print(j)
    print(k)
