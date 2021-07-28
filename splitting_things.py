pangram = "The quick brown fox jumps over the lazy dog"

words = pangram.split()

print(words)

numbers = "9,223,372,036,854,775,807"

num_list = numbers.split(",")

for index, number in enumerate(num_list):
    num_list[index] = int(number)

print(num_list)


nums = input("Enter three integers, separated by ','")
num_list = nums.split(",")
print(int(num_list[0]) + int(num_list[1]) - int(num_list[2]))