# student_grade_calculator.py
# Beginner Python project to calculate student grade with validation

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better 😊"
    elif marks >= 60:
        return "D", "You passed! Keep practicing 💪"
    else:
        return "F", "Don't worry! Learn from mistakes and try again 💡"


# Input student name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    marks = input("Enter marks (0-100): ")

    if marks.isdigit():
        marks = int(marks)
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100.")
    else:
        print("❌ Please enter a valid number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print(f"\n📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
