# Assignment 3: Employee Access Control System  

# Sample Input:  

employees = [  
"EMP001:John_Smith:Engineering:SENIOR",  
"EMP002:Sarah_Johnson:HR:MANAGER",  
"EMP003:Mike_Brown:Finance:JUNIOR",  
"EMP004:Lisa_Davis:Engineering:MANAGER",  
"EMP005:Tom_Wilson:Security:SENIOR"  
]  
department_access_rights = {  
"Engineering": {"LAB", "SERVER_ROOM", "OFFICE", "PARKING"},  
"HR": {"HR_OFFICE", "OFFICE", "PARKING", "MEETING_ROOM"},  
"Finance": {"FINANCE_OFFICE", "OFFICE", "PARKING"},  
"Security": {"ALL_AREAS"}  
}  
access_logs = [  
"EMP001:LAB:SUCCESS:09:15",  
"EMP002:HR_OFFICE:SUCCESS:09:30",  
"EMP003:SERVER_ROOM:FAILED:10:00",  
"EMP001:SERVER_ROOM:SUCCESS:10:15",  
"EMP004:LAB:SUCCESS:11:00",  
"EMP005:FINANCE_OFFICE:SUCCESS:11:30", 
"EMP002:SERVER_ROOM:FAILED:12:00",  
"EMP003:FINANCE_OFFICE:SUCCESS:14:00"  
] 



# 1. Validate employee credentials and departments  

employee_dict = {}
for employee in employees:
    emp_data = employee.split(":")
    emp_id = emp_data[0]
    emp_name = emp_data[1]
    emp_department = emp_data[2]
    emp_role = emp_data[3]
    employee_dict[emp_id] = {
        "name": emp_name,
        "department": emp_department,
        "role": emp_role
    }
    print(f"Employee ID: {emp_id}, Name: {emp_name}, Department: {emp_department}, Role: {emp_role}")   

# 2. Track access attempts (successful and failed)


for log in access_logs:
    log_data = log.split(":")
    emp_id = log_data[0]
    access_area = log_data[1]
    access_status = log_data[2]
    access_time = log_data[3] + ":" + log_data[4]

    if emp_id in employee_dict:
        emp_department = employee_dict[emp_id]["department"]
        if access_area in department_access_rights.get(emp_department, set()):
            print(f"Access Attempt: Employee ID: {emp_id}, Area: {access_area}, Status: {access_status}, Time: {access_time}")
        else:
            print(f"Access Denied: Employee ID: {emp_id}, Area: {access_area}, Status: {access_status}, Time: {access_time}")
    else:
        print(f"Invalid Employee ID: {emp_id}, Area: {access_area}, Status: {access_status}, Time: {access_time}")


# 3. Identify security violations (access to unauthorized areas)  

access_violations = []
for log in access_logs:
    log_data = log.split(":")
    emp_id = log_data[0]
    access_area = log_data[1]
    access_status = log_data[2]
    access_time = log_data[3] + ":" + log_data[4]

    if emp_id in employee_dict:
        emp_department = employee_dict[emp_id]["department"]
        if access_area not in department_access_rights.get(emp_department, set()):
            access_violations.append({
                "emp_id": emp_id,
                "access_area": access_area,
                "access_status": access_status,
                "access_time": access_time
            })
            print(f"Security Violation: Employee ID: {emp_id}, Area: {access_area}, Status: {access_status}, Time: {access_time}")

# 4. Generate access reports by department 

access_reports = {}
for log in access_logs:
    log_data = log.split(":")
    emp_id = log_data[0]
    access_area = log_data[1]
    access_status = log_data[2]
    access_time = log_data[3] + ":" + log_data[4]

    if emp_id in employee_dict:
        emp_department = employee_dict[emp_id]["department"]
        if emp_department not in access_reports:
            access_reports[emp_department] = []
        access_reports[emp_department].append({
            "emp_id": emp_id,
            "access_area": access_area,
            "access_status": access_status,
            "access_time": access_time
        })

        print(f"Access Report: Department: {emp_department}, Employee ID: {emp_id},Area: {access_area}, Status: {access_status}, Time: {access_time}")
        