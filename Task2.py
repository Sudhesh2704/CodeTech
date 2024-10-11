# Program to Track and Manage Student Grades

def calculate_letter_grade(average):
    if average >= 90:
        return 'A', 4.0
    elif average >= 80:
        return 'B', 3.0
    elif average >= 70:
        return 'C', 2.0
    elif average >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

def input_grades():
    grades = {}
    subjects_count = int(input("Enter the number of subjects or assignments: "))
    
    for i in range(subjects_count):
        subject = input(f"Enter the name of subject or assignment #{i+1}: ")
        grade = float(input(f"Enter the grade for {subject} (0-100): "))
        grades[subject] = grade
    
    return grades

def calculate_average(grades):
    total = sum(grades.values())
    return total / len(grades)

def display_grades(grades, average, letter_grade, gpa):
    print("\n--- Grade Report ---")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    
    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.1f}")

def main():
    print("Welcome to the Student Grade Tracker!")
    
    # Step 1: Input grades
    grades = input_grades()
    
    # Step 2: Calculate the average grade
    average = calculate_average(grades)
    
    # Step 3: Determine letter grade and GPA
    letter_grade, gpa = calculate_letter_grade(average)
    
    # Step 4: Display results
    display_grades(grades, average, letter_grade, gpa)

# Running the program
if __name__ == "__main__":
    main()
