# print(parrot)

# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

# print()

# print(parrot[-1])
# print(parrot[-14])

# print()

# print(parrot[-11])
# print(parrot[-1])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# print()

# print(parrot[3 - 14])
# print(parrot[4 - 14])
# print(parrot[9 - 14])
# print(parrot[3 - 14])
# print(parrot[6 - 14])
# print(parrot[8 - 14])

# parrot = "Norwegian Blue"

# print(parrot[0:6])
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])
# print(parrot[0:])
# print(parrot[10:])

# print(parrot[:6] + parrot[6:])
# print(parrot[:])

# print(parrot[-4:-2])
# print(parrot[-4:12])

# print(parrot[-14:-8])

# print(parrot[0:6:2])
# print(parrot[0:6:3])


# print(number[1::4])

# separators = number[1::4]
# print(separators)

# number = "9,223;372:036 854,775;807"

number = input("Please enter a series of numbers, using any separators you like: ")

separators = ""

for char in number:
    if not char.isnumeric():
        separators += char


values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])
print(sum([int(val) for val in values]))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for char in quote:
    if char.isupper():
        print(char)