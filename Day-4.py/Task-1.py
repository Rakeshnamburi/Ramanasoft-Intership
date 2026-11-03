# 1. Student Management System (SMS) – CRUD with Functions, List & Dictionary 


# 1. Functions (Modular Programming) 
# o Breaking the program into smaller functions (add_student, display_students, update_student, 
# delete_student)

# 1. Student Management System (SMS) – CRUD with Functions, List & Dictionary 
# Scenario: 
# A college needs a Student Management System to maintain student records such as ID, Name, Age, and Course. 
# The system should allow the administrator to: 
# • Add new students (Create) 
# • Display all students (Read) 
# • Update student details (Update) 
# • Delete student records (Delete) 
# The program should be menu-driven and use Python functions with list + dictionary to store and manage student data. 
# Topics Covered: 
# This project helps practice: 
# 1. Functions (modular programming) 
# 2. Lists (to store multiple student records) 
# 3. Dictionaries (to represent student details as key-value pairs) 
# 4. CRUD operations (Create, Read, Update, Delete) 
# 5. Loops and Conditionals (menu-driven system) 
# 6. String and Integer handling (input validation, updates) 
# Task Objectives: 
# This project helps practice: 
# 1. Functions (Modular Programming) 
# o Breaking the program into smaller functions (add_student, display_students, update_student, 
# delete_student). 
# 2. Lists 
# o Storing multiple student records inside a single list (students = []). 
# 3. Dictionaries 
# o Representing each student as a dictionary ({"id": "S101", "name": "Ravi", "age": 20, "course": 
# "B.Tech"}). 
# 4. CRUD Operations 
# o Create → Add new student 
# o Read → Display all students 
# o Update → Modify details 
# o Delete → Remove student 
# 5. input() Function Usage 
# o Taking user input for ID, Name, Age, Course. 
# 6. Loops & Conditionals (Menu-Driven System) 
# o Using a while True: loop for continuous menu display. 
# o Using if-elif-else for menu choices. 
# 7. String & Integer Handling (Input Validation & Updates) 
# o Converting age input (int(input("Enter Age: "))). 
# o Skipping updates when user presses Enter. 
# o Validating student IDs before update/delete.


# e project ke asalike em kavali ante, student management system create cheyali ante CRUD operations implement cheyali.
# crud ante create, read, update, delete operations implement cheyali.
# code 1st ela start cheyali ante 1st students data ni list lo store cheyali, prathi student data ni dictionary lo store cheyali.
# next step ela cheyali ante, menu driven system create cheyali, user ki options ivvali, add student, display students, update student, delete student.
# a next step ela cheyali ante, prathi option ki function create cheyali, add_student(), display_students(), update_student(), delete_student().
# prathi function lo input() function use chesi user input ni collect cheyali, age ni int() lo convert cheyali, and prathi student data ni dictionary lo store chesi list lo append cheyali.
# loops deniki use cheyali ante, while True loop use chesi menu display cheyali, if-elif-else use chesi user choice ki corresponding function call cheyali.
# sring and integer handling deniki use cheyali ante, input validation cheyali, user enter chesina data ni check cheyali, age ni int() lo convert cheyali, updates ki user press Enter chesina case handle cheyali.





students = [
    {"id": "S101", "name": "Rakesh", "age": 20, "gender": "Male", "course": "B.Tech"},
    {"id": "S102", "name": "Namburi", "age": 22, "gender": "Female", "course": "MBA"},
    {"id": "S103", "name": "Manasavi", "age": 19, "gender": "Female", "course": "B.Sc"},
    {"id": "S104", "name": "Pooja", "age": 21, "gender": "Female", "course": "BCA"}
]

# ekkada manam data motham list,tuple,integer , string type lo diff methods lo tisukonam
# ekkada nuchi taruvata output print avatam ala motham vastundhi 
# e code lo students list create chesam, prathi student data ni dictionary lo store chesam, and list lo append chesam.

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    gender = input("Enter Student Gender: ")
    course = input("Enter Student Course: ")


# ekkada emo student dictionary create chesam, and list lo append chesam, and print message ivvali.
#  manaki output lo seperate ga ravali ante ekkada ela seperate print ani easte ela vastundhi

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "gender": gender,
        "course": course
    }

# ekkada string and integer handling chesam, age ni int() lo convert chesam, 
# and input validation cheyali ante user enter chesina data ni check cheyali.

    students.append(student)
    print("Student added successfully!")

# ekkada append endhuku use chesam ante list lo element add chesam.
# add chesetapudu append ani use cheyali taruvata print added sucessfully message ivvali.

def display_students():
    if len(students) == 0:
        print("No students found")
    else:
        print("\nStudent List")
        for student in students:
            print(
                f"ID: {student['id']}, Name: {student['name']}, "
                f"Age: {student['age']}, Gender: {student['gender']}, Course: {student['course']}"
            )

# ekkada nuchi em chestundhi ante ekkada ela seperate print ani easte ela vastundhi
# len function use chesam ante students list lo elements count chesam, if-else use chesam ante students list empty unte "No students found" message print cheyali, else lo for loop use chesam ante prathi student data ni print cheyali.
# len(students) == 0 ante students list empty unte, print("No students found") message ivvali, else lo for loop use chesam ante prathi student data ni print cheyali.
# \n student List message ivvali, for loop lo f-string use chesam ante prathi student data ni format chesam, and print cheyali.
# id and age before f endhuku use chesam ante prathi student data ni format chesam, and print cheyali.
# e lines vala uses enti ante 


def update_student():
    student_id = input("Enter Student ID to update: ")


    for student in students:
        if student["id"] == student_id:

            new_name = input("Enter new name (leave blank to skip): ")
            new_age = input("Enter new age (leave blank to skip): ")
            new_gender = input("Enter new gender (leave blank to skip): ")
            new_course = input("Enter new course (leave blank to skip): ")

            if new_name:
                student["name"] = new_name

            if new_age:
                student["age"] = int(new_age)

            if new_gender:
                student["gender"] = new_gender  

            if new_course:
                student["course"] = new_course

            print("Student updated successfully!")
            return

    print("Student not found")



# ekkada nunchi taruvata output print avatam ala motham vastundhi
# i.e output lo manaki seperate ga vastundhi ga so ekkada manam rasam kabate ela seperate ga vastundhi

def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Invalid gender! Please enter a valid gender.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")

# ekkada elif endhuku use chesam ante user enter chesina choice 1-5 range lo lekapothe "Invalid Choice" message ivvali.


#    OUTPUT

# ===== Student Management System =====
# 1. Add Student
# 2. Display Students
# 3. Update Student
# 4. Delete Student
# 5. Exit
# Enter your choice: 1
# Enter Student ID: S105
# Enter Student Name: Rakesh
# Enter Student Age: 23
# Enter Student Course: MBBS
# Student added successfully!

# ===== Student Management System =====
# 1. Add Student
# 2. Display Students
# 3. Update Student
# 4. Delete Student
# 5. Exit
# Enter your choice: 2

# Student List
# ID: S101, Name: Ravi Kumar, Age: 20, Course: B.Tech
# ID: S102, Name: Anita Sharma, Age: 22, Course: MBA
# ID: S103, Name: Vikram Singh, Age: 19, Course: B.Sc
# ID: S104, Name: Priya Mehta, Age: 21, Course: BCA
# ID: s103, Name: Vikram Singh, Age: 19, Course: B.sc
# ID: S105, Name: Rakesh, Age: 23, Course: MBBS

# ===== Student Management System =====
# 1. Add Student
# 2. Display Students
# 3. Update Student
# 4. Delete Student
# 5. Exit
# Enter your choice: 

# Student List
# ID: S101, Name: Rakesh, Age: 20, Gender: Male, Course: B.Tech
# ID: S102, Name: Namburi, Age: 22, Gender: Female, Course: MBA
# ID: S103, Name: Manasavi, Age: 19, Gender: Female, Course: B.Sc
# ID: S104, Name: Pooja, Age: 21, Gender: Female, Course: BCA
# ID: 105, Name: Priya, Age: 27, Gender: female, Course: MBBS
