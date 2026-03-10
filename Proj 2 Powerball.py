import random
def generate_powerball_numbers():
    #Welcome user and asking them if they want to generate PowerBall numbers.
    print ("Welcome to the PowerBall number generator.")
    print ("Would you like some PowerBall numbers?") 
    answer = input("(Yes/No): ")

    # Function for random generation of white ball possibilities.
    white_possibilities = random.sample(range(1,70), k=5)
    white_possibilities.sort()
    # Function for the random generation of the red powerball number.
    powerball = random.randint(1,26)
    return white_possibilities, powerball
# Close the function; Generate Numbers
white_possibilities, powerball = generate_powerball_numbers()
print (f"Your PowerBall numbers are: {white_possibilities[0]}  {white_possibilities[1]}  {white_possibilities[2]}  {white_possibilities[3]}  {white_possibilities[4]}    {powerball}")
print ("Thanks for using the PowerBall number generator. Goodbye!")
