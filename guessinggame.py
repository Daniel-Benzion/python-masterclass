answer = 5

print("Guess a number between 1 and 10: ")

while True:
    guess = int(input())

    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print("You got it!")
        break

tree1 = 'Oak'
tree2 = 'Ash'

if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different")