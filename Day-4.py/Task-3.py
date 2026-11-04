# 3. Pharmacy Inventory System using the functions



# Features of the Pharmacy Inventory System:

# 1. Add Medicine 
# o Enter details like Medicine ID, Name, Price, Quantity, Expiry Date. 
# o Saves the medicine record in the inventory list and CSV file. 


import csv
from datetime import date

from decorator import append
from sqlalchemy import false

medicines = []
suppliers = []
sales = []


# ekkada medicine.csv file create chesukovali. File lo medicine details store cheyali.
# sales.csv file create chesukovali. File lo sales details store cheyali.
# suppliers.csv file create chesukovali. File lo suppliers details store cheyali.
# .csv file lo manama eche commands motham store itai andhuke csv use chestaru

#1     Add Medicine



def add_medicine():

    medicine_id = input("Enter Medicine ID : ")
    medicine_name = input("Enter Medicine Name : ")
    price = int(input("Enter Price : "))
    quantity = int(input("Enter Quantity : "))
    expiry_date = input("Enter Expiry Date (YYYY-MM-DD) : ")

    medicine = {
        "id": medicine_id,
        "name": medicine_name,
        "price": price,
        "quantity": quantity,
        "expiry": expiry_date
    }

    medicines.append(medicine)

    file = open("medicines.csv", "a", newline="")
    writer = csv.writer(file)

    writer.writerow(
        [medicine_id, medicine_name, price, quantity, expiry_date]
    )

    file.close()

    print("Medicine Added Successfully")


# ekkada add medicine function lo medicine.csv file create chesukovali. File lo medicine details store cheyali.
# medicines ke releated ina name,id,date of manufacture,expiry date,price,quantity details store cheyali.
# writer.writerow() function use chesi medicine details store cheyali.
# endhuku eppudu csv file lo details store chesuko.ndhuku 
# newlinw="" ante new line lo store cheyali ani artham.
# file.close() ante file close cheyali ani artham.append endhuku use chesaru ante file lo new data add cheyali ani artham.


#    2    Search Medicine



def search_medicine():

    medicine_name = input("Enter Medicine Name : ")

    found = False

    for medicine in medicines:

        if medicine["name"].lower() == medicine_name.lower():

            print("\nMedicine Found")
            print("ID :", medicine["id"])
            print("Name :", medicine["name"])
            print("Price :", medicine["price"])
            print("Quantity :", medicine["quantity"])
            print("Expiry :", medicine["expiry"])

            found = True
            break

    if found == False:
        print("Medicine Not Found")


# ekkada found variable use chesaru ante medicine name search chesinappudu medicine found ayithe true avuthundi. lekapothe false avuthundi.
# break use chesaru ante medicine found ayithe loop nunchi exit avuthundi. lekapothe loop continue avuthundi. 


#    3     Update Medicine


def update_medicine():

    medicine_id = input("Enter Medicine ID To Update : ")

    found = False

    for medicine in medicines:

        if medicine["id"] == medicine_id:

            new_price = input("Enter New Price : ")
            new_quantity = input("Enter New Quantity : ")
            new_expiry = input("Enter New Expiry Date : ")

            if new_price != "":
                medicine["price"] = int(new_price)

            if new_quantity != "":
                medicine["quantity"] = int(new_quantity)

            if new_expiry != "":
                medicine["expiry"] = new_expiry

            print("Medicine Updated Successfully")

            found = True
            break

    if found == False:
        print("Medicine Not Found")



# ekkada update medicine function lo medicine id use chesaru ante medicine id search chesinappudu medicine found ayithe new price, new quantity, new expiry date update avuthundi. lekapothe medicine not found ani print avuthundi.
# expiry date update chesinappudu new expiry date empty kakapothe update avuthundi. lekapothe previous expiry date untundi.
# quantity update chesinappudu new quantity empty kakapothe update avuthundi. lekapothe previous quantity untundi.

#      4         Add Supplier



def add_supplier():

    supplier_id = input("Enter Supplier ID : ")
    supplier_name = input("Enter Supplier Name : ")
    contact = input("Enter Contact Number : ")
    company = input("Enter Company Name : ")

    supplier = {
        "id": supplier_id,
        "name": supplier_name,
        "contact": contact,
        "company": company
    }

    suppliers.append(supplier)

    print("Supplier Added Successfully")




# ekkada supplier id, supplier name, contact number, company name details store chesaru. suppliers list lo store chesaru. lekapothe supplier not found ani print avuthundi.   
# append use chesaru ante suppliers list lo new supplier add avuthundi. lekapothe previous suppliers list untundi.
# ekkada evaru supplu chestrunaru vala details avi motham save intai. lekapothe supplier not found ani print avuthundi.   



# Calculate Total Sale
def total_sale():

    medicine_id = input("Enter Medicine ID : ")
    quantity_sold = int(input("Enter Quantity Sold : "))

    found = False

    for medicine in medicines:

        if medicine["id"] == medicine_id:

            if quantity_sold <= medicine["quantity"]:

                sale_value = quantity_sold * medicine["price"]

                medicine["quantity"] = (
                    medicine["quantity"] - quantity_sold
                )

                month = input("Enter Month (MM-YYYY) : ")

                sales.append({
                    "month": month,
                    "amount": sale_value
                })

                print("Sale Recorded Successfully")
                print("Total Sale Value :", sale_value)

            else:
                print("Not Enough Stock")

            found = True
            break

    if found == False:
        print("Medicine Not Found")



# ekkada total sale function lo medicine id use chesaru ante medicine id search chesinappudu quantity sold check chesaru. lekapothe medicine not found ani print avuthundi.   
# found variable use chesaru ante medicine id search chesinappudu medicine found ayithe true avuthundi. lekapothe false avuthundi.
# quantity sold check chesinappudu quantity sold less than or equal to medicine quantity untundante sale value calculate chesaru. lekapothe not enough stock ani print avuthundi. 
# append use chesaru ante sales list lo new sale add avuthundi. lekapothe previous sales list untundi.    
# ekkada sales entha indhi out flow entha entha order remeaning undhi entha quantity manaki kavali ani motham details ekkada vastundhu

# Monthly Sales




def monthly_sales():

    month = input("Enter Month (MM-YYYY) : ")

    total = 0

    for sale in sales:

        if sale["month"] == month:
            total = total + sale["amount"]

    print("Total Sales For", month, ":", total)



# ekkada nuchi store ke monthly sales and purchase details motham store chesaru. lekapothe total sales for month print avuthundi.
    # ekkada total variable use chesaru ante month lo total sales calculate chesaru. lekapothe total sales for month print avuthundi.



# total purchase from the medical distributor and total sales to the customer for the month. The difference between the two will be the profit for the month.

# Total purchase from compnay = 0
# Total sales to customer = 0

# Main Menu
while True:

    print("\n===== Pharmacy Inventory System =====")
    print("1. Add Medicine")
    print("2. Search Medicine")
    print("3. Update Medicine")
    print("4. Add Supplier")
    print("5. Calculate Total Sale")
    print("6. Calculate Monthly Sales")
    print("7. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        add_medicine()

    elif choice == 2:
        search_medicine()

    elif choice == 3:
        update_medicine()

    elif choice == 4:
        add_supplier()

    elif choice == 5:
        total_sale()

    elif choice == 6:
        monthly_sales()

    elif choice == 7:
        print("Exiting Pharmacy Inventory System")
        break

    else:
        print("Invalid Choice")