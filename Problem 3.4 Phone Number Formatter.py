def format_phone_number():
    # Get input from the user
    user_input = input("Enter phone: ")

    # Filter for only numeric characters
    digits = "".join(filter(str.isdigit, user_input))

    # Result check for 10 digits
    if len(digits) == 10:
        area_code = digits[:3]
        prefix = digits[3:6]
        line_number = digits[6:]
        formatted = f"({area_code}) {prefix}-{line_number}"
        print(f"Formatted: {formatted}")
        # Else statement for invalid input
    else:
        print("Invalid phone number (must be 10 digits)")

if __name__ == "__main__":
    format_phone_number()
