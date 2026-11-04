# # Store application 

# # 1.  Write a programming to view items, add items, purchase items, search items, edit items, exit. 

# items = []


# def add_items():
#     item = input("Enter Item Name: ")
#     items.append(item)
#     print("Item Added Successfully")
#     print("Items Displayed Successfully")
#     else:
#     for item in items:
#         print(item) 

# def purchase_items():
#     item = input("Enter Item Name: ")
#     if item in items:
#         items.remove(item)
#         print("Item Purchased Successfully")
#     else:
#         print("Item Not Found")

# def search_items():
#     item = input("Enter Item Name: ")
#     if item in items:
#         print("Item Found")
#     else:
#         print("Item Not Found")

# def edit_items():
#     old_item = input("Enter Old Item Name: ")
#     if old_item in items:
#         new_item = input("Enter New Item Name: ")
#         items[items.index(old_item)] = new_item
#         print("Item Edited Successfully")
#     else:
#         print("Item Not Found")

# def exit():
#     print("Exiting Store Application")



# Supermarket Management System

items = []

# View Items
def view_items():

    print("\nView Items")

    print("The number of items in inventory are :", len(items))

    if len(items) == 0:
        print("No items available")

    else:
        for item in items:
            print("Name :", item["name"])
            print("Quantity :", item["quantity"])
            print("Price :", item["price"])
            print("-----------------")


# Add Items
def add_items():

    print("\nAdd Items")

    name = input("Item Name : ")
    quantity = int(input("Item Quantity : "))
    price = int(input("Price : "))

    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    items.append(item)

    print("Item Added Successfully")


# Purchase Items
def purchase_item():

    print("\nPurchase Items")

    item_name = input("Enter Item Name : ")

    found = False

    for item in items:

        if item["name"].lower() == item_name.lower():

            if item["quantity"] > 0:

                item["quantity"] = item["quantity"] - 1

                print("Pay", item["price"], "at checkout counter")

            else:

                print("Item Out Of Stock")

            found = True
            break

    if found == False:
        print("Item Not Found")


# Search Item
def search_item():

    print("\nSearch Item")

    item_name = input("Enter Item Name To Search : ")

    found = False

    for item in items:

        if item["name"].lower() == item_name.lower():

            print("Item Found")
            print(item)

            found = True
            break

    if found == False:
        print("Item Not Found")


# Edit Item
def edit_item():

    print("\nEdit Item")

    item_name = input("Enter Item Name To Edit : ")

    found = False

    for item in items:

        if item["name"].lower() == item_name.lower():

            print("Current Details")
            print(item)

            new_name = input("Enter New Name : ")
            new_quantity = int(input("Enter New Quantity : "))
            new_price = int(input("Enter New Price : "))

            item["name"] = new_name
            item["quantity"] = new_quantity
            item["price"] = new_price

            print("Item Updated Successfully")

            found = True
            break

    if found == False:
        print("Item Not Found")


# Main Menu

while True:

    print("\n===== Supermarket Management System =====")
    print("1. View Items")
    print("2. Add Items")
    print("3. Purchase Items")
    print("4. Search Items")
    print("5. Edit Items")
    print("6. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        view_items()

    elif choice == 2:
        add_items()

    elif choice == 3:
        purchase_item()

    elif choice == 4:
        search_item()

    elif choice == 5:
        edit_item()

    elif choice == 6:
        print("Exited Successfully")
        break

    else:
        print("Invalid Choice")
