import datetime

#  Obtain information from user
name = input("Enter your name: ")
age_num = input("Enter your age: ")
city = input("Enter your city: ")

# Change age into an int 
age = int(age_num)
#use function to create equation for finding birth age
present_year = datetime.date.today().year
birth_year = present_year - age

# Print final output sentences; name, age, city, birth year
print("\n Personal Information Display ")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"City: {city}")
print(f"Your Birth Year is: {birth_year}")
