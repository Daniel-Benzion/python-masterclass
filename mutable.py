# Python has the following built-in mutable objects:
# list
# dict
# set
# Bytearray

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]


another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]

print(shopping_list)

print(id(shopping_list))
print(id(another_list))

a = b = c = d = shopping_list

print(a)
b.append("flour")
print(a)
print(d)
c.append("apples")
print(d)