# task :-5 Employee anlysis system


# Problem Statement: 
 
#  You are developing an HR analytics system. Employee performance data is stored as tuples 
# containing: (employee_id, name, department, monthly_sales, rating). You need to analyze this data 
# to provide insights for management decisions.


# Sample Input:  
 
import code


employees = [ (1001, "Alice Johnson", "Sales", 15000, 4.2),  
(1002, "Bob Smith", "Sales", 12000, 3.8),  
(1003, "Carol Davis", "Marketing", 8000, 4.5),  
(1004, "David Brown", "Sales", 18000, 4.0),  
(1005, "Eva Wilson", "Marketing", 9500, 3.2),  
(1006, "Frank Miller", "IT", 11000, 3.9),  
(1007, "Grace Lee", "Sales", 13500, 2.1),  
(1008, "Henry Taylor", "IT", 10500, 4.1),  
(1009, "Ivy Chen", "Marketing", 7800, 3.7),  
(1010, "Jack Davis", "IT", 12500, 3.5) ]


# 1. Find the top 3 performers by sales in each department 
departments = {}
for emp in employees:
    dept = emp[2]
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(emp)

for dept, emp_list in departments.items():
    top_performers = sorted(emp_list, key=lambda x: x[3], reverse=True)[:3]
    print(f"Top 3 performers in {dept}:")
    for emp in top_performers:
        print(f"  {emp[1]} - ${emp[3]} - {emp[4]}")

        # ekkada x:x[3] endhuku use chesaru ante x[3  ] ante employee tuple lo 4th index lo unna monthly_sales ni refer chesthundi. 
        # So, sorting ki use chesthunnaru.
        # code lo x[3] ante employee tuple lo 4th index lo unna monthly_sales ni refer chesthundi. So, sorting ki use chesthunnaru.
        # top 3 performers ni department wise sort chesi print chesthunnaru.
        # emp_list endhuku use chesaru ante department wise employees list ni store chesthundi.
        # dep = emp[2] endhuku use chesaru ante department name ni refer chesthundi. adhi ela refer chestundhi ante emp tuple lo 3rd index lo department name untundi. So, emp[2] use chesaru.




# 2. Calculate average rating for each department  

avg_ratings = {}
for dept, emp_list in departments.items():
    total_rating = sum(emp[4] for emp in emp_list)
    avg_rating = total_rating / len(emp_list)
    avg_ratings[dept] = avg_rating

for dept, avg_rating in avg_ratings.items():
    print(f"Average rating in {dept}: {avg_rating:.2f}")



    # emp[4 ] ante employee tuple lo 5th index lo unna rating ni refer chesthundi. So, average rating calculate cheyadaniki use chesthunnaru.
    # sum(emp[4] for emp in emp_list) endhuku use chesaru ante department wise employees list lo unna rating values ni sum cheyadaniki use chesthunnaru.
    # avg _rating = total_rating / len(emp_list) endhuku use chesaru ante department wise employees list lo unna rating values ni average calculate cheyadaniki use chesthunnaru.
    


# 3. Identify employees who need performance improvement (rating < 3.0) 

rating_threshold = 3.0
improvement_needed = [emp for emp in employees if emp[4] < rating_threshold]

print("Employees who need performance improvement:")
for emp in improvement_needed:
    print(f"  {emp[1]} - {emp[4]}")

    # ekkada emp[4] endhuku use chesaru ante employee tuple lo 5th index lo unna rating ni refer chesthundi. So, performance improvement ki use chesthunnaru. 
    # print(f"  {emp[1]} - {emp[4]}") endhuku use chesaru ante employee name and rating ni print cheyadaniki use chesthunnaru.    
    # emp[4] < rating_threshold endhuku use chesaru ante employee tuple lo 5th index lo unna rating value ni compare cheyadaniki use chesthunnaru. 
    # So, performance improvement ki use chesthunnaru.
    # thresold = 3.0 endhuku use chesaru ante performance improvement ki threshold value ni set cheyadaniki use chesthunnaru. 


# 4. Create a ranked list of all employees by their performance score (sales * rating) 

sales_rating = [(emp[0], emp[1], emp[2], emp[3] * emp[4]) for emp in employees]
ranked_employees = sorted(sales_rating, key=lambda x: x[3], reverse=True)

print("Ranked employees by performance score:")
for emp in ranked_employees:
    print(f"  {emp[1]} - {emp[3]}") 

    # ekkada sales_rating endhuku use chesaru ante employee details lo unna sales and rating values ni combine chesaru.
    # ranked_employees endhuku use chesaru ante employee details lo unna performance score ni based on sort chesi store chesthundi.
    # print(f"  {emp[1]} - {emp[3]}") endhuku use chesaru ante employee name and performance score ni print cheyadaniki use chesthunnaru.
    # 4th input lo emp[3] endhuku use chesaru ante employee tuple lo 4th index lo unna performance score ni refer chesthundi. So, print cheyadaniki use chesthunnaru.
    