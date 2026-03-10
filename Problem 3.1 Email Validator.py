# Start by requesting an email address from the user.
inquiry = input("Enter an email address: ")
# Define what a valid email is; create if, else statements for each criteria
def valid_email(email):
    if email.count('@') != 1:
        return False
    if ' ' in email:
        return False
    if email.lower() != email:
        return False
    at_index = email.index('@')
    if '.' not in email[at_index:]:
        return False
    return True
# After validating the email address, print whether it is valid or not.
if valid_email(inquiry):
    print("Valid email address.")
else: print("Invalid email address:")
