# for i in range(1, 13):
#     print("# {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#     print("*" * 40)

name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {} years".format(18 - age))

# if age < 18:
#     print("Please come back in {} years".format(18 - age))
# else:
#     print("You are old enough to vote")

if age < 18:
    print("Please come back in {} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")