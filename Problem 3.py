import random

def random_number_guesser():

    real_number = random.randint(1, 10)
    
    # Ask for user to guess #, provide conditional if incorrect
    user_guess_str = input("Guess a number between 1 and 10: ")
    user_guess = int(user_guess_str)

    # Tell the user what the actual number was
    print(f"The number was actually {real_number}.")

    # Conditionals 
    if user_guess == real_number:
        print("Great job! You guessed the right number!")
    else:
        print("Sorry, that wasn't correct.")

if __name__ == "__main__":
    random_number_guesser()
