import random

def play_game():
    # Generate a random number between 1 & 50
    secret_number = random.randint(1, 50)
    attempts = 7
    
    print("I'm thinking of a number between 1-50")
    print(f"You have {attempts} guesses")

    for i in range(1, attempts + 1):
        #  Get user input
        try:
            guess = int(input(f"Guess #{i}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check guess
        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print(f"Correct! You got it in {i} guesses!")
            return

    #Out of guesses
    print(f"Game over! The number was {secret_number}.")

if __name__ == "__main__":
    play_game()
