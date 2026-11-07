
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

prelim = float(input("Enter Prelim grade: "))
midterm = float(input("Enter Midterm grade: "))
finals = float(input("Enter Finals grade: "))

average = (prelim + midterm + finals) / 3

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
