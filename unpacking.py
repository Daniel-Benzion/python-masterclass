a = b = c = d = e = f = 12

data = 1, 2, 3
x, y, z = data
print(x)
print(y)
print(z)

data_list = [12, 13, 14]
p, q, r = data_list
print(p)
print(q)
print(r)


for index, character in enumerate("abcdefgh"):
    print(index, character)

for t in enumerate("abcdefgh"):
    print(t)

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)