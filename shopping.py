shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)

item_to_find = "spam"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at:
    print("Found item({}) at index {}".format(item_to_find, found_at))
else:
    print("Item({}) not found".format(item_to_find))



