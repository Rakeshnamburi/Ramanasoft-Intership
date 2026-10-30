# Task 2: Student Attendance and Exam Eligibility


print("***** Student Attendance Details *****")

name = input("Enter student's name: ")
total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))

attendance_percentage = (attended_classes / total_classes) * 100

print(f"Attendance percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("Student is eligible for the exam.")
else:
    print("Student is not eligible for the exam.")


    
    