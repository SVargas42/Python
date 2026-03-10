def test_help ():
    answer_key = "1=A, 2=A, 3=C, 4=B"
    user_answer = input("Would you like the answer key for the test? " \
    "If so, please input the password: ")
    if user_answer == "Password123":
        print (answer_key)

test_help()