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

test_case_list = ['A', 'b', 'F', 'd', 't', 'P', 'z', 'G']
print(sorted(test_case_list, key=str.casefold))






empty_list = []

num2 = [1, 3, 5, 7, 9]
num3 = [2, 4, 6, 8, 10]


num4 = num2 + num3

sort_nums = sorted(num4)

print(sort_nums)

digits = sorted("432985617")
print(digits)

digits2 = list(digits)

print(digits2)

print(digits == digits2)
print(digits is digits2)

digits3 = digits.copy()

print(digits == digits3)
print(digits is digits3)


empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]


for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)