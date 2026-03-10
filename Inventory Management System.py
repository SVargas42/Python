#Project 3: Inventory Management System
#Due Tuesday
# Build a complete inventory management system using dictionaries and functions.

"""
Inventory Management System 
DS 3850 - Thursday Project 3
Selena Vargas
"""

# Dictionary; I included the items from the example in the directions.
inventory = [
    {"name": "Laptop", "category": "Electronics", "quantity": 10, "price": 999.99},
    {"name": "Mouse", "category": "Electronics", "quantity": 25, "price": 24.99},
    {"name": "Desk", "category": "Furniture", "quantity": 5, "price": 249.99}
]
# Menu Display Function
def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print(" INVENTORY MANAGEMENT SYSTEM")
    print("="*40)
    print("1. View all products")
    print("2. Add new product")
    print("3. Update quantity")
    print("4. Search product")
    print("5. Remove product")
    print("6. Calculate inventory value")
    print("7. Low stock alert")
    print("8. Exit")
    print("="*40)

def view_all_products(inventory):
    """Display all products in a formatted table."""
    if not inventory:
        print("\nInventory is currently empty.")
        return

    # Table header
    print("\n" + "-"*60)
    print(f"| {'Name':<15} | {'Category':<15} | {'Quantity':<8} | {'Price':<10} |")
    print("-" * 60)

    # Print each product in the inventory
    for product in inventory:
        print(f"| {product['name']:<15} | {product['category']:<15} | {product['quantity']:<8} | ${product['price']:<9.2f} |")
    print("-" * 60)

def add_product(inventory):
    """Add a new product to the inventory after validation."""
    print("\n--- Add New Product ---")
    while True:
        name = input("Enter product name: ").strip().capitalize()
        if not name:
            print("Product name cannot be empty. Please try again.")
            continue

        # Duplicate check: Ensure product name is unique (case-insensitive)
        if any(p['name'] == name for p in inventory):
            print(f"Error: Product '{name}' already exists in inventory. Use the update option instead.")
            return

        category = input("Enter category: ").strip().capitalize()

        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer for quantity.")

        while True:
            try:
                price = float(input("Enter price: $"))
                if price <= 0:
                    print("Price must be a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a positive number for price.")

        new_product = {
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price
        }
        inventory.append(new_product)
        print(f"\nSuccessfully added '{name}' to inventory.")
        return

def update_quantity(inventory):
    """Update quantity for an existing product."""
    if not inventory:
        print("\nInventory is empty. Cannot update quantity.")
        return

    print("\n--- Update Product Quantity ---")
    name = input("Enter product name to update quantity: ").strip().capitalize()
    #Product search and update logic
    product_found = False
    for product in inventory:
        if product['name'] == name:
            product_found = True
            print(f"Current quantity for '{name}': {product['quantity']}")
            while True:
                try:
                    new_quantity = int(input("Enter new quantity: "))
                    if new_quantity < 0:
                        print("Quantity cannot be negative.")
                        continue
                    product['quantity'] = new_quantity
                    print(f"Successfully updated quantity for '{name}' to {new_quantity}.")
                    return
                except ValueError:
                    print("Invalid input. Please enter an integer.")

    if not product_found:
        print(f"Product '{name}' not found in inventory.")

def search_product(inventory):
    """Search and display product by name."""
    if not inventory:
        print("\nInventory is empty. Cannot search.")
        return

    print("\n--- Search Product ---")
    name = input("Enter product name to search: ").strip().capitalize()

    found_products = [p for p in inventory if name.lower() in p['name'].lower()]

    if found_products:
        print(f"\nFound {len(found_products)} matching product(s):")
        for product in found_products:
            print(f"- Name: {product['name']}, Category: {product['category']}, Quantity: {product['quantity']}, Price: ${product['price']:.2f}")
    else:
        print(f"No product found matching '{name}'.")

def remove_product(inventory):
    """Remove a product from the inventory."""
    if not inventory:
        print("\nInventory is empty. Cannot remove product.")
        return

    print("\n--- Remove Product ---")
    name = input("Enter product name to remove: ").strip().capitalize()

    original_count = len(inventory)
    # Use list comprehension to create a new list excluding the product to be removed
    inventory[:] = [product for product in inventory if product['name'] != name]

    if len(inventory) < original_count:
        print(f"Successfully removed '{name}' from inventory.")
    else:
        print(f"Product '{name}' not found in inventory.")
# Inventory value calculation and low stock alert functions; return function included
def calculate_inventory_value(inventory):
    """Return the total value of all inventory and display it."""
    total_value = sum(product['quantity'] * product['price'] for product in inventory)
    print(f"\nTotal inventory value: ${total_value:,.2f}")
    return total_value 

def low_stock_alert(inventory, threshold=5):
    """Display products below the specified threshold quantity."""
    if not inventory:
        print("\nInventory is empty.")
        return

    print(f"\n--- Low Stock Alert (Threshold < {threshold} units) ---")
    low_stock_items = [p for p in inventory if p['quantity'] < threshold]

    if low_stock_items:
        for product in low_stock_items:
            print(f"- Name: {product['name']}, Quantity: {product['quantity']} units remaining.")
    else:
        print("All products are well stocked.")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == '1':
            view_all_products(inventory)
        elif choice == '2':
            add_product(inventory)
        elif choice == '3':
            update_quantity(inventory)
        elif choice == '4':
            search_product(inventory)
        elif choice == '5':
            remove_product(inventory)
        elif choice == '6':
            calculate_inventory_value(inventory)
        elif choice == '7':
            low_stock_alert(inventory, threshold=5)
        elif choice == '8':
            print("\nThank you for using Inventory Manager! Goodbye.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
