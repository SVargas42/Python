num_students = int(input("How many students? "))

# Set variables
total_score = 0
highest_grade = None
lowest_grade = None

# Loop to get grades and update statistics
for i in range(1, num_students + 1):
    grade = float(input(f"Enter grade for student {i}: "))
    
    # Need total score for average calculation
    total_score += grade
    
    # if statements for highest and lowest grades; set highest_grade and lowest_grade to None initially
    if highest_grade is None or grade > highest_grade:
        highest_grade = grade
    if lowest_grade is None or grade < lowest_grade:
        lowest_grade = grade

# Calculate average
average_grade = total_score / num_students

# Final Display of grades
print("\n=== GRADE STATISTICS ===")
print(f"Average: {average_grade:.2f}")
print(f"Highest: {highest_grade}")
print(f"Lowest: {lowest_grade}")
