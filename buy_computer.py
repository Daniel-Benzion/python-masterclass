current_choice = "-"
available_parts = ["computer", "monitor", "keyboard", "mouse", "mousepad", "HDMI cable"]
computer_parts = []

while current_choice != "0":
    if current_choice in "123456":
        print("Adding {}".format(available_parts[int(current_choice) - 1]))
        computer_parts.append(available_parts[int(current_choice) - 1])       
    else:
        print("Please add options from the list below or select 0 to exit:")
        for number, part in enumerate(available_parts):
            print("{}: {}".format(number + 1, part))

    current_choice = input()

print(computer_parts)


data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for plant in data:
    #name = plant[:plant.index("-") - 1]
    if plant[plant.index("-") + 2:] == "Flower":
        flowers.append(plant)
    else:
        shrubs.append(plant)