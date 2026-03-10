import math

# Thursday Project 1: Business Discount Qualifier

    # Name: [Selena Vargas]
    # Date: [1/22/2026]

def calculate_discounts():
    print("========================================")
    print("      DISCOUNT QUALIFICATION SYSTEM     ")
    print("========================================")

    # 1. Collect Information
    name = input("Enter customer name: ")
    purchase_amount = float(input("Enter purchase amount: $"))
    is_loyalty_str = input("Is customer a loyalty member? (yes/no): ").lower()
    is_loyalty = is_loyalty_str == 'yes'

    years_member = 0
    if is_loyalty:
        years_member = int(input("How many years as a member?: "))

    is_birthday_str = input("Is it their birthday month? (yes/no): ").lower()
    is_birthday = is_birthday_str == 'yes'
    
    is_first_time_str = input("Is this their first purchase? (yes/no): ").lower()
    is_first_time = is_first_time_str == 'yes'
    
    age = int(input("Enter customer age: "))

    # Initialize variables
    total_discount_pct = 0.0
    applied_discounts = []
    loyalty_applied = False

    # 2. Calculate Discounts Based on Rules

    # A. Loyalty Member Discounts
    if is_loyalty:
        if years_member >= 5 and purchase_amount > 100:
            total_discount_pct += 0.20
            applied_discounts.append("Gold Member Discount: 20%")
            loyalty_applied = True
        elif 2 <= years_member <= 4 and purchase_amount > 100:
            total_discount_pct += 0.15
            applied_discounts.append("Silver Member Discount: 15%")
            loyalty_applied = True
        elif 0 <= years_member <= 1 and purchase_amount > 150:
            total_discount_pct += 0.10
            applied_discounts.append("Bronze Member Discount: 10%")
            loyalty_applied = True

    # First-Time Customer discount
    if is_first_time and not loyalty_applied:
        total_discount_pct += 0.10
        applied_discounts.append("First-Time Customer Discount: 10%")

    # Volume Discounts 
    if not loyalty_applied:
        if purchase_amount > 500:
            total_discount_pct += 0.25
            applied_discounts.append("Volume Discount (>500): 25%")
        elif purchase_amount > 300:
            total_discount_pct += 0.15
            applied_discounts.append("Volume Discount (>300): 15%")
        elif purchase_amount > 150:
            total_discount_pct += 0.10
            applied_discounts.append("Volume Discount (>150): 10%")

    #Special Occasion (Birthday Month)
    if is_birthday:
        total_discount_pct += 0.05
        applied_discounts.append("Birthday Bonus: 5%")

    # Senior Citizen Discount
    if age >= 65:
        total_discount_pct += 0.05
        applied_discounts.append("Senior Discount: 5%")

    # Discount Cap
    if total_discount_pct > 0.35:
        total_discount_pct = 0.35

    # Final amount calculation
    discount_amount = purchase_amount * total_discount_pct
    final_price = purchase_amount - discount_amount

    # Receipt
    print("\n========================================")
    print("          DISCOUNT BREAKDOWN            ")
    print("========================================")
    print(f"Customer: {name}")
    print(f"Original Amount: ${purchase_amount:.2f}")
    print("Discounts Applied:")
    if not applied_discounts:
        print("- None")
    else:
        for discount in applied_discounts:
            print(f"- {discount}")
    print("------------------------")
    print(f"Total Discount: {total_discount_pct:.0%}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")
    print("Thank you for shopping with us!")

# Run the system
if __name__ == "__main__":
    calculate_discounts()
