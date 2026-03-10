def countdown():
     # Ask for input, convert it to an integer
    start_number_str = input("Enter starting number: ")
    start_number = int(start_number_str)

    # Check if the number is positive
    if start_number <= 0:
        print("Please enter a positive integer.")
        return

    # Loop for number countdown
    for i in range(start_number, 0, -1):
        print(i)

    # "Blast off!" after the loop finishes
    print("Blast off!")

if __name__ == "__main__":
    countdown()
