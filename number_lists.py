even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print("Mississippi".count("s"))
print("Mississippi".count("iss"))


even.extend(odd)
print(even)


even.sort()
print(even)

even.sort(reverse=True)
print(even)

even2 = sorted(even)

nums = [2.3, 21, 16, 1.7]

print(sorted(nums))


test = ["a", "n", "b", "p", "g", "d", "t"]

test2 = sorted(test)

print(test)
print(test2)

print()

print(id(test))
print(id(test2))