def gen(n):
    n += 1
    yield n


g = gen(500)
for i in g:
    print(i)
