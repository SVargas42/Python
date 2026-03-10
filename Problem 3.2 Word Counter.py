# Ask for user to input a sentence
sentence = input("Enter a sentence: ")

# Calculate the total number of words in the sentence; 
# split the sentence into a list of words and count the length of the list
words_list = sentence.split()
total_words = len(words_list)
total_characters = len("".join(words_list))

# Uppercase conversion
uppercase_sentence = sentence.upper()
# Lowercase conversion
lowercase_sentence = sentence.lower()

# Print the results
print("\nTotal words:", total_words)
print("Total characters:", total_characters)
print("Uppercase:", uppercase_sentence)
print("Lowercase:", lowercase_sentence)
