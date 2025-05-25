# MENU OF RESTAURANT
menu = {
    "pizza": 90,
    "Burger": 60,
    "samosa": 30,
    "salad": 70,
    "coffee": 80,
    "chicken": 100,
    "saahi panner": 110,
    "sweet": 70
}

print("Welcome to my Restaurant")
print("pizza : RS90\nBurger : RS60\nsamosa : RS30\nsalad : RS70\ncoffee : RS80\nchicken : RS100\nsaahi panner : RS110\nsweet : RS70")

order_total = 0

item_1 = input("Enter the name of the item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item (yes/no): ")

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount to pay is: RS{order_total}")
print("!! Thank you !!")
