name = input("What is your name? ")
age = int(input("How many years old are you, {}? ".format(name)))

if (17 < age < 31):
    print("Welcome to the holiday!")
else:
    if (age > 30):
        print("You're too old!!!!!")
    else:
        if (age == 17):
            print("Come back next year")
        else:
            print("Come back in {} years".format(18 - age))