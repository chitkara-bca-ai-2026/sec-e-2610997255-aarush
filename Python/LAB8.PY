print("=" * 40)
print("       SCHOOL RESULT PROCESSING")
print("=" * 40)

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

marks = []
print("\n--- Enter Marks for 5 Subjects (0-100) ---")

for i in range(1, 6):
    m = int(input(f"Enter marks for Subject {i}: "))

    if m < 0 or m > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    marks.append(m)

total = sum(marks)
percentage = total / 5

if any(m < 40 for m in marks):
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"

    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"

print("\n" + "=" * 40)
print("          STUDENT REPORT CARD")
print("=" * 40)
print("Student Name :", name)
print("Roll Number  :", roll)
print("-" * 40)
print(f"Total Marks  : {total:.1f} / 500.0")
print(f"Percentage   : {percentage:.2f}%")
print("Result       :", result)
print("Grade        :", grade)
print("Remarks      :", remark)
print("=" * 40)
