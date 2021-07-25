# Python has several built-in data types, which can be classed as:
#   > numeric
#   > iterator
#   > sequence (which are also iterators)
#   > mapping
#   > file
#   > class
#   > exception

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print()

for i in range(1, 4):
    print(i)

for i in range(1, a // b):
    print(i)


bun_price = 2.40
money = 15
print(money // bun_price)