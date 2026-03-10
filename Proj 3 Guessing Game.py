import random
def number_guessing_game():
    # Define functions
    secret_number = random.randint(1,10)
    attempts = 0
    question = "Hello! Would you like to play a number guessing game? (yes/no): "
    user_response = input(question)
    # Begin by asking the user if they want to play or not.
    if user_response == "yes":
      print("Great! Please guess a number from 1 to 10.")
      # If yes, then the game will begin.
    elif user_response == "no":
      print("No worries, maybe next time!")
      # Return feature to end game
      return
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number within the range of 1 to 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Great job! You guessed the number {secret_number} in {attempts} attempts.")
                print("Thank you for playing the Number Guessing Game. See you next time!")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
if __name__ == "__main__":

    number_guessing_game()

    