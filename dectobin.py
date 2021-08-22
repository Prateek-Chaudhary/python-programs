# b = int(input("enter the number\n"))
# def dtob(n):
#     if n>1:
#         dtob(n//2)
#     print(n%2, end="")
# if __name__ == "__main__":
#     dtob(b)
# print()

ls = []
print("enter the numbers")
i = 1
while i<=4:
    l = int(input())
    i = i + 1
    if l % 5 == 0:
        b_n = bin(l)
        ls.append(b_n)
print(ls)