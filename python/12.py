products = [
    ["Coffee Beans", 25],
    ["Green Tea Box", 15],
    ["Chocolate Cookies", 12],
    ["Milk Bottle", 8],
    ["Orange Juice", 10],
    ["Honey Jar", 30],
    ["Olive Oil", 45],
    ["Pasta Pack", 6],
    ["Cheese Block", 20],
    ["Strawberry Jam", 18]
]
print("Choose a product number:\n")
for i, item in enumerate(products, start=1):
    print(f"{i} - {item[0]}")
choice = int(input("\nEnter the number: "))

if choice < 1 or choice > len(products):
    print("Invalid number!")
    exit()


selected_price = products[choice - 1][1]
tax = selected_price * 0.15
total = selected_price + tax

print(f"\nProduct price including tax: {total}")