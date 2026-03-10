def simple_calculator():
 # Get two numbers from the user

    num1_val = input("Enter the first number: ")
    num2_val = input("Enter the second number: ")

    # input conversion to float
    num1 = float(num1_val)
    num2 = float(num2_val)

    sum_result = num1 + num2
    diff_result = num1 - num2

    # Format and display results- remember, needs to be formatted with numbers to 2 decimal places
    
    print(f"The sum of ${num1:.2f} and ${num2:.2f} is: ${sum_result:.2f}")
    print(f"The difference of ${num1:.2f} and ${num2:.2f} is: ${diff_result:.2f}")
    

# Run calc
if __name__ == "__main__":
    simple_calculator()
