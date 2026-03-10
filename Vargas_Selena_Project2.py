# Thursday Project 2: Sales Tracker

    # Name: [Selena Vargas]
    # Date: [2/5/2026]
sales_list = []
    # Print functions for menu options
while True:
    print("\n" + "=" * 40)
    print("SALES TRACKER SYSTEM")
    print("=" * 40)
    print("\n1. View all sales")
    print("2. Add daily sale")
    print("3. Calculate total sales")
    print("4. Calculate average sale")
    print("5. Find best day")
    print("6. Find worst day")
    print("7. Show days above average")
    print("8. Exit")
    print("=" * 40)

    choice = input("\nChoice: ")
    # Implement menu options with if-elif statements
    # Option 1: View all sales
    if choice == "1":
        if not sales_list:
            print("No sales data yet!")
        else:
            for i, sale in enumerate(sales_list, 1):
                print(f"Day {i}: ${sale:,.2f}")
            print(f"Total entries: {len(sales_list)}")
    #Option 2: Add daily sale; I added error handling for more than 7 days
    elif choice == "2":
        if len(sales_list) >= 7:
            print("Cannot add more than 7 days!")
        else:
            try:
                amount = float(input("Enter sale amount: $"))
                if amount <= 0:
                    print("Amount must be positive!")
                else:
                    sales_list.append(amount)
                    print(f"Added sale for Day {len(sales_list)}: ${amount:,.2f}")
            except ValueError:
                print("Invalid input! Please enter a number.")
    # Option 3: Calculate total sales
    elif choice == "3":
        if not sales_list:
            print("No sales data yet!")
        else:
            total = sum(sales_list)
            print(f"Total sales: ${total:,.2f}")
    # Option 4: Calculate average sale
    elif choice == "4":
        if not sales_list:
            print("No sales data yet!")
        else:
            avg = sum(sales_list) / len(sales_list)
            print(f"Average daily sale: ${avg:,.2f}")
    # Option 5: Find best day
    elif choice == "5":
        if not sales_list:
            print("No sales data yet!")
        else:
            best_val = max(sales_list)
            day_num = sales_list.index(best_val) + 1
            print(f"Best Day: Day {day_num} with ${best_val:,.2f}")
    # Option 6: Find worst day
    elif choice == "6":
        if not sales_list:
            print("No sales data yet!")
        else:
            worst_val = min(sales_list)
            day_num = sales_list.index(worst_val) + 1
            print(f"Worst Day: Day {day_num} with ${worst_val:,.2f}")
    # Option 7: Show days above average
    elif choice == "7":
        if not sales_list:
            print("No sales data yet!")
        else:
            avg = sum(sales_list) / len(sales_list)
            print(f"Average is ${avg:,.2f}. Days above average:")
            count = 0
            for i, sale in enumerate(sales_list, 1):
                if sale > avg:
                    print(f"  Day {i}: ${sale:,.2f}")
                    count += 1
            print(f"Total days above average: {count}")
    # Option 8: Exit; thank you message printed as well
    elif choice == "8":
        print("Thank you for using the Sales Tracker!")
        break

    else:
        print("Invalid choice! Please select 1-8.")
