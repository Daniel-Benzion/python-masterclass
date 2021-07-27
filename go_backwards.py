data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200


for i in range(len(data) - 1, -1, -1):
    if data[i] < 100 or data[i] > 200:
        del data[i]

print(data)