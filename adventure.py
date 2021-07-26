available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ").casefold()
    if chosen_exit == "quit":
        print("Game over")
        break

print("Aren't you glad you got out of there?")


# Coding Exercise 10: Break
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

# Coding Exercise 11: Continue
for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)