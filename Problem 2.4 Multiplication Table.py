# Ask for user input
num = int(input("Enter a number: "))

print(f"Multiplication Table for {num}:")

# Table and Loop for 1-12; include 13 for range
for i in range(1, 13):
    result = num * i
    print(f"{num} x {i} = {result}")
