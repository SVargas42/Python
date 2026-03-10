import random

def run_quiz():
    questions = {
        "What is the tallest mountain in the world?": "Mount Everest",
        "What is the world's most populated city?": "Tokyo, Japan",
        "Which U.S. state grows coffee beans?": "Hawaii",
        "Who painted the Mona Lisa?": "Leonardo da Vinci",
        "What was the first vegetable ever to be grown in space?": "Potato"
    }

    score = 0
    question_keys = list(questions.keys())
    # Shuffle question order
    random.shuffle(question_keys) 

    print("Welcome to the Quiz Bowl Game! Do you have what it takes to answer all questions correct?")
    print("Answer the following questions to test your knowledge.")

    for question in question_keys:
        print(f"\nQuestion: {question}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == questions[question].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {questions[question]}")

    print(f"\nQuiz finished! You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()