# Task 2: Employee Data Processing and Aggregation  


employee_data = [  
(101, "Alice Smith", "Engineering", 90000, 5),  
(102, "Bob Johnson", "Marketing", 75000, 3),  
(103, "Charlie Brown", "Engineering", 120000, 8),  
(104, "Diana Prince", "HR", 65000, 2),  
(105, "Edward King", "Marketing", 80000, 5),  
(106, "Frank Castle", "Engineering", 95000, 0), # 0 years of service  
]




# (1) Sort by Salary: Create a new list of employees sorted by salary in descending order. 

# \nsort(salary) in descending order.
# sorted_by_salary = sorted(employee_data, key=lambda x: x[3], reverse=True)
# for log in sorted_by_salary:
#     print(log)



# salary_sorted = sorted(employee_data, key=lambda x: x[3], reverse=True)

# print("Sorted by Salary:")
# for emp in salary_sorted:
#     print(emp)

    # ekkada use chesina technique enti ante lambda function use chesi prathi employee entry lo salary ni key ga use chesi descending order lo sort chesthundi.
    # x: x[3] ante prathi employee tuple lo 4th element (salary) ni key ga use chesthundi. reverse=True ante descending order lo sort chesthundi.
    # key declaration lo lambda function use chesi prathi employee entry lo salary ni key ga use chesi descending order lo sort chesthundi.
    # and valu una salary nee descending order lo petali





#     2. Sort by Years of Service (then Name): Create a new list of employees sorted first by years 
# of service (descending) and then by name (ascending) for ties. 


service_sorted = sorted(employee_data, key=lambda x: (-x[4], x[1]))

print("\nSorted by Service:")
for emp in service_sorted:
    print(emp)

#     ekkada valaki em kavali ante una data yers ne chusukoni big to small order lo sort chesi, same years of service unna employees ni name ascending order lo sort chesthundi.
#     \n sorted() function lo key declaration lo lambda function use chesi prathi employee entry lo years of service ni negative ga use chesi descending order lo sort chesthundi.
# -x[4] ante prathi employee tuple lo 5th element (years of service) ni negative ga use chesi descending order lo sort chesthundi. x[1] ante prathi employee tuple lo 2nd element (name) ni ascending order lo sort chesthundi.


# 3. Calculate Statistics:  
# o Calculate the total salary expenditure.   (salary adigaru)
# o Find the minimum and maximum salary.  (max and min salary adigaru)
# o Find the average years of service.     (avg of employment years of service adigaru)

# total_salary = sum(emp[3] for emp in employee_data)
# min_salary = min(emp[3] for emp in employee_data)
# max_salary = max(emp[3] for emp in employee_data)
# avg_service = sum(emp[4] for emp in employee_data) / len(employee_data)  


#  4 endhuku use chesaru ante, sum() function use chesi prathi employee entry lo salary ni add chesi total salary calculate chesthundi. min() and max() functions use chesi prathi employee entry lo salary ni compare chesi minimum and maximum salary find chesthundi. average years of service calculate cheyadaniki, sum() function use chesi prathi employee entry lo years of service ni add chesi total years of service calculate chesthundi, then total years of service ni employee_data list length tho divide chesthundi to get average.
# 0,1,2,3, ga use cheyali

# print("\nStatistics")
# print("Total Salary:", total_salary)
# print("Minimum Salary:", min_salary)
# print("Maximum Salary:", max_salary)
# print("Average Service:", avg_service)




# 4. Identify High Earners: Create a list of names of employees earning more than $90,000.  

high_earners = [emp[1] for emp in employee_data if emp[3] > 90000]
print("\nHigh Earners:")
for name in high_earners:
    print(name)

    # 90000 salary ekkuva earn chese employees names list create cheyadaniki, list comprehension use chesi prathi employee entry lo salary check chesthundi. 
    # If salary > 90000, employee name ni list lo add chesthundi. Final ga, high_earners list lo names print chesthundi.


# 5. Remove an Employee: An employee with employee_id=104 has left the company. Remove 
# their record from the employee_data list. (Use del after finding the index).  

index_to_remove = next((i for i, emp in enumerate(employee_data) if emp[0] == 104), None)
if index_to_remove is not None:
    del employee_data[index_to_remove]
    print("\nEmployee with ID 104 removed.")


    # akkada em adigaru ante id-104 ne remove cheyamanaru so adhi index lo undhi  and 0 put lo undhi kabate
    # x-0 remove ipoina taruvata none ani ravali inka em rakodadu 





#     6. Data Validation Checks:  
# o Use all() to check if all employees have at least 1 year of service.  
# o Use any() to check if any employee in "Engineering" earns less than $70,000.




# 1 year of service check cheyadaniki, all() function use chesi prathi employee entry lo years of service check chesthundi. 
# If all employees have at least 1 year of service, True return chesthundi; otherwise, False.





service_sorted = sorted(employee_data, key=lambda x: (-x[4],))

print("\nSorted by Service:")
for emp in service_sorted:
    print(emp)


less_earners = [emp[1] for emp in employee_data if emp[3] < 700000]
print("\nless Earners:")
for name in less_earners:
    print(name)


    