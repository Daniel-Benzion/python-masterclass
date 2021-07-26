day = "Monday"
temperature = 30
raining = True

def activities():
    if day == "Saturday" and temperature > 27 and not raining:
        print("Go swimming")
    else:
        print("Learn Python")

activities()

day = "Saturday"
raining = False

activities()