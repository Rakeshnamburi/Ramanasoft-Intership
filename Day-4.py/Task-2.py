# 2. Extended Student Management System – With Subject Marks 

# Scenario 
# The college now wants to track marks of 5 subjects for each student. 
# The admin should be able to: 
# • Select a student by ID 
# • Enter marks for 5 subjects (Math, Science, English, Computer, History) 
# • Store these marks in the student’s record for future use (like calculating average, topper list, etc.) 
# Topics Covered 
# In addition to the previous ones: 
# 1. Nested Dictionary Handling → Storing subject marks inside each student’s dictionary. 
# 2. Input Validation → Accepting integer marks for each subject. 
# 3. List & Dictionary Update → Adding a "marks" key to the student dictionary. 
# 4. Function Reusability → New function add_student_marks(). 
# Sample Data with Marks: 
# Before marks added: 
# {"id": "S101", "name": "Ravi Kumar", "age": 20, "course": "B.Tech"}


# After marks added:
# {"id": "S101", "name": "Ravi Kumar", "age": 20, "course": "B.Tech", "marks": {"Math": 85, "Science": 90, "English": 78, "Computer": 92, "History": 88}} 


students = [
    {"id": "S101", "name": "Ravi Kumar", "age": 20, "course": "B.Tech"},
    {"id": "S102", "name": "Anita Sharma", "age": 22, "course": "MBA"}
]


def add_marks():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            marks = {
                "Math": int(input("Enter Math Marks: ")),
                "Science": int(input("Enter Science Marks: ")),
                "English": int(input("Enter English Marks: ")),
                "Computer": int(input("Enter Computer Marks: ")),
                "History": int(input("Enter History Marks: "))
            }

            student["marks"] = marks

            print("Marks Added Successfully")
            return

    print("Student Not Found")


def display_students():
    for student in students:
        print(student)


add_marks()
display_students()



# Enter Student ID: S101
# Enter Math Marks: 20
# Enter Science Marks: 35
# Enter English Marks: 67
# Enter Computer Marks: 50
# Enter History Marks: 84
# Marks Added Successfully
# {'id': 'S101', 'name': 'Ravi Kumar', 'age': 20, 'course': 'B.Tech', 'marks': {'Math': 20, 'Science': 35, 'English': 67, 'Computer': 50, 'History': 84}}
# {'id': 'S102', 'name': 'Anita Sharma', 'age': 22, 'course': 'MBA'}
# PS D:\Ramansoft answers\vscode daywise\Day-1.py> 