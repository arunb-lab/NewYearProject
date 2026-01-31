inventory = {
    "pen": {"price": 10, "stock": 50},
    "copy": {"price": 80, "stock": 20},
    "pencil": {"price": 5, "stock": 100}
}

cart = {}

while True:
    print("\n1) Show items  2) Buy  3) Checkout  4) Exit")
    choice = input("Choose: ")

    if choice == "1":
        print("\n--- INVENTORY ---")
        for item, data in inventory.items():
            print(f"{item} -> Rs {data['price']} | stock: {data['stock']}")

    elif choice == "2":
        item = input("Item name: ").lower()
        if item not in inventory:
            print("Not available.")
            continue

        qty = int(input("Quantity: "))
        if qty <= 0:
            print("Invalid quantity.")
            continue

        if qty > inventory[item]["stock"]:
            print("Not enough stock.")
            continue

        inventory[item]["stock"] -= qty
        cart[item] = cart.get(item, 0) + qty
        print("Added to cart.")

    elif choice == "3":
        print("\n--- BILL ---")
        total = 0
        for item, qty in cart.items():
            price = inventory[item]["price"]
            cost = price * qty
            total += cost
            print(f"{item} x{qty} = Rs {cost}")
        print("TOTAL =", total)
        cart.clear()
        print("Checkout complete.")

    elif choice == "4":
        break

    else:
        print("Invalid option.")
