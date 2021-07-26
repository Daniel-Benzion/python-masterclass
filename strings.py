print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + ' world')
greeting = "Hello"
name = input("Please enter your name: ")
print(greeting + ' ' + name)

print(type(greeting))

age = 24
print(age)
print(type(age))

# age = "two years"
# print(age)
# print (type(age))

# print(name + " is " + age + " years old.")
print(name + " is " + str(age) + " years old.")

print(name + f"is {age} years old")
print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")