inventory = {}
    # List of options; loop until user chooses to exit
while True:
    print("\n1. View all products\n2. Add product\n3. Update quantity\n4. Search product\n5. Exit")
    choice = input("Choice: ")
    # Handle each choice with if-elif statements
    if choice == '1':
        print("=== INVENTORY ===")
        if not inventory:
            print("Inventory is empty.")
        for product, qty in inventory.items():
            print(f"{product}: {qty} units")

    elif choice == '2':
        name = input("Product name: ")
        qty = int(input("Quantity: "))
        inventory[name] = inventory.get(name, 0) + qty
        print(f"Added {name} ({qty} units)")

    elif choice == '3':
        name = input("Product to update: ")
        if name in inventory:
            new_qty = int(input("New quantity: "))
            inventory[name] = new_qty
            print(f"Updated {name} to {new_qty} units")
        else:
            print("Product not found.")

    elif choice == '4':
        name = input("Search for: ")
        if name in inventory:
            print(f"✓ Found: {name} ({inventory[name]} units)")
        else:
            print("Product not found.")

    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice, try again.")
