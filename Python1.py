def play_madlibs():
    print("Hello!")
    print("Please enter words below in the corresponding prompts to create your own Madlib story!")
    
    # Provide prompts for users to enter words
    adjective = input("Enter an adjective: ")
    large_objects_plural = input("Enter large objects (plural): ")
    body_part = input("Enter a body part: ")
    noun = input("Enter a restaurant: ")
    first_food = input("Enter a food: ")
    second_food = input("Enter another food: ")
    large_object = input("Enter a large object: ")
    
    # Create story base for players
    story = f"I’ve had a very {adjective} day." \
    f" This morning, I dropped a box of {large_objects_plural} on my {body_part}." \
    f" Then, at lunch, I went to {noun} for their delicious {first_food}," \
    f" But the waiter brought me {second_food}, which I was not hungry for." \
    f" Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."

    # Print finished Madlib
    print("\nHere's your Mad Libs story:")
    print(story)

# Call the function to start the game
play_madlibs()