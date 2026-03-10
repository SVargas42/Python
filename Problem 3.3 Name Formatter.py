import re

def format_name(messy_name):
   # Remove extra spaces and capitalize the first letter of each name component
    cleaned_name = " ".join(messy_name.strip().split())
    
    # Capitalize the first letter of each name component
    capitalized_name = cleaned_name.title()
    
    # Split the name into components
    names = capitalized_name.split()
    # Name formatting
    if len(names) == 2:
        first_name, last_name = names
        middle_initial = ""
    elif len(names) >= 3:
        first_name = names[0]
        middle_initial = names[1][0].upper() + "." 
        last_name = names[-1]
        # Returns error message if user enters only one name
    else:
        return "Please enter at least first and last name" 
    
    # Format as "Last, First M."
    if middle_initial:
        formatted_name = f"{last_name}, {first_name} {middle_initial}"
    else:
        formatted_name = f"{last_name}, {first_name}"
        
    return formatted_name

# Example Usage:
messy_name = input("Please enter your name:")

print(f"Original: '{messy_name}' -> Formatted: '{format_name(messy_name)}'")

