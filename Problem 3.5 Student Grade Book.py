def student_grade_book():
    grades = {}
    # If-While loop to get student names and grades until 'done' is entered
    while True:
        name = input("Enter student name (or 'done'): ").strip()
        if name.lower() == 'done':
            break
        # Try-except block to handle non-numeric grade input
        try:
            score = float(input(f"Enter grade for {name}: "))
            grades[name] = score
        except ValueError:
            print("Invalid input. Please enter a numerical grade.")
    
    if not grades:
        print("No data entered.")
        return

    # Grade average, highest, and lowest
    avg_grade = sum(grades.values()) / len(grades)
    highest_student = max(grades, key=grades.get)
    lowest_student = min(grades, key=grades.get)

    # Print the grade book; Student name, grade, class average
    print("\n=== GRADE BOOK ===")
    for student, grade in grades.items():
        print(f"{student}: {grade}")
    
    print(f"Class Average: {avg_grade:.2f}")
    print(f"Highest: {highest_student} ({grades[highest_student]})")
    print(f"Lowest: {lowest_student} ({grades[lowest_student]})")

if __name__ == "__main__":
    student_grade_book()
