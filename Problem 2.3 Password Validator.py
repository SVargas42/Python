def is_valid_password(password):
    # Check length
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
        return False
    
    # Check for at least one number
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break # Exit the loop once a number is found
            
    if not has_number:
        print("Password must contain at least one number!")
        return False
        
    # Password valid if both conditions are met
    return True

while True:
    user_password = input("Create a password: ")
    if is_valid_password(user_password):
        print("Password accepted!")
        break 

