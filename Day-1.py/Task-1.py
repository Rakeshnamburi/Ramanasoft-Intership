print("*** Student Personal Information ***")

name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
mobile_number = input("Enter Student Mobile Number: ")
email_id = input("Enter Student Email ID: ")
department = input("Enter StudentDepartment: ")
roll_number = input("Enter Student Roll Number: ")
city = input("Enter Student City: ")


# ekkada manaki student nuchi em kavali avi motham vaka string input lo store chesukovali.
# adhi only akkada ina data variki store chesukontundhi


print("\n*** Student Personal Information ***")
python_marks = int(input("Enter Python Marks: "))
java_marks = int(input("Enter Java Marks: "))
database_marks = int(input("Enter Data Base Marks: "))
datascience_marks = int(input("Enter Data Science Marks: "))
web_marks = int(input("Enter Web Development Marks: "))

total_marks = python_marks + java_marks + database_marks + datascience_marks + web_marks
average_marks = total_marks / 5

# ekkada nuchi em jarugutundhi ante student marks ni input chesukuntunnam. akkada nundi manaki marks kavali avi motham integer lo store chesukovali. 
# adhi only akkada ina data variki store chesukontundhi.   int(input()) function use chesi manam integer lo store chesukuntunnam.
# ekkada orginal  marks enthake conduct chesamo rayatam kosam e code radam



print("\n*** Student Marks ***")
python_marks = int(input("Enter Python Marks: "))
java_marks = int(input("Enter Java Marks: "))
database_marks = int(input("Enter Data Base Marks: "))
datascience_marks = int(input("Enter Data Science Marks: "))
web_marks = int(input("Enter Web Development Marks: "))

# ekkada em ante original student ke eni marks marks vachai ane daniki manam enter cheyataniki student marks ni input chesukuntunnam.
# akkada nundi manaki marks kavali avi motham integer lo store chesukovali.

total_marks = python_marks + java_marks + database_marks + datascience_marks + web_marks
average_marks = total_marks / 5

# ekkada emo total marks and average marks calculate chesukuntunnam. 
# total marks ante python, java, database, datascience, web development marks ni add chesi total marks calculate chesukuntunnam. average marks ante total marks ni 5 tho divide chesi average marks calculate chesukuntunnam.

if (python_marks >= 35 and
    java_marks >= 35 and
    database_marks >= 35 and
    datascience_marks >= 35 and
    web_marks >= 35):

    # min 35 marks vaste below vaste fail ani ardham

    result = "Pass"

    if average >= 75:
        grade = "Distinction"

    elif average >= 60:
        grade = "First Class"

    elif average >= 50:
        grade = "Second Class"

    else:
        grade = "Pass"

else:
    result = "Fail"
    grade = "Fail"




    print("\n***** Student Personal Information *****")

print("Full Name      :", name)
print("Age            :", age)
print("Mobile Number  :", mobile)
print("Email ID       :", email)
print("Department     :", department)
print("Roll Number    :", roll_no)
print("City           :", city)

print("\n***** Student Marks *****")

print("Python         :", python_marks)
print("Java           :", java_marks)
print("Data Base      :", database_marks)
print("Data Science   :", datascience_marks)
print("Web Development:", web_marks)

print("\nTotal Marks    :", total)
print("Average Marks  :", round(average, 2))
print("Result         :", result)
print("Grade          :", grade)

