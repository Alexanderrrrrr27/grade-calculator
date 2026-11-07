
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

grades = []

for subject in ["Prelim", "Midterm", "Finals"]:
    while True:
        try:
            grade = float(input(f"Enter {subject} grade: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Please enter a grade from 0 to 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")

average = sum(grades) / len(grades)

print("\n===== GRADE RESULT =====")
print("Student Name:", name)
print("Average Grade:", round(average, 2))

if average >= 90:
    print("Rating: Excellent")
elif average >= 85:
    print("Rating: Very Good")
elif average >= 80:
    print("Rating: Good")
elif average >= 75:
    print("Rating: Passed")
else:
    print("Rating: Failed")

print("\nThank you for using the Grade Calculator!")
