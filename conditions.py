age = int(input("How old are you?"))

if age >= 16 and age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your freedom")

if age < 16 or age > 65:
    print("Enjoy your freedom")
else:
    print("Have a good day at work")

if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your freedom")

if not(16 <= age <= 65):
    print("Enjoy your freedom")
else:
    print("Have a good day at work")