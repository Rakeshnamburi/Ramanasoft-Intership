# 4. Pharmacy Inventory System – Billing Feature: 

medicines = [
    {"id": "M101", "name": "Paracetamol", "price": 10, "discount": 10, "quantity": 100},
    {"id": "M102", "name": "Ibuprofen", "price": 15, "discount": 5, "quantity": 50},
    {"id": "M103", "name": "Amoxicillin", "price": 20, "discount": 15, "quantity": 30},
    {"id": "M104", "name": "Cetirizine", "price": 12, "discount": 6, "quantity": 80},
    {"id": "M105", "name": "Metformin", "price": 25, "discount": 20, "quantity": 40}
]


# ekkada emo data store chesam, and list lo append chesam, and print message ivvali.

generated_bill = []
customer_name = input("Enter Customer Name: ")
customer_contact = input("Enter Customer Contact: ")
discount = float(input("Enter Discount Percentage: "))
case = input("Enter Case (e.g., Regular, Emergency): ")
count = int(input("Enter number of medicines to purchase: "))


# ekkada nuchi emo generate bill list create chesam, and for loop use chesam ante user enter chesina medicines count varaku repeat chesam, 
# and medicine id, quantity, discount percentage input tisukoni bill generate chesam. manaki output lo separate ga ravali ante ekkada ela separate print ani easte ela vastundhi, 
# and medicine id check chesam ante medicines list lo medicine id match ayithe bill generate chesam, lekapothe "
# Medicine ID not found." message print cheyali, and medicine quantity check chesam ante available quantity compare chesam, lekapothe "Insufficient stock" message print cheyali,
# and medicine price calculate chesam ante medicine price * quantity, and discount apply chesam ante total price - (total price * discount percentage / 100), and medicine quantity update chesam ante available quantity - purchased quantity, 
# and bill print chesam ante medicine name, quantity, price, total price, and grand total calculate chesam ante sum of all total prices.  




for _ in range(count):
    medicine_id = input("Enter Medicine ID: ")
    quantity = int(input("Enter Quantity: "))
    discount_percentage = float(input("Enter Discount Percentage for this medicine: "))


# ekkada nuchi emo for loop use chesam ante user enter chesina medicines count varaku repeat chesam, and medicine id, quantity, discount percentage input tisukoni bill generate chesam. 
# manaki output lo separate ga ravali ante ekkada ela separate print ani easte ela vastundhi, and medicine id check chesam ante medicines list lo medicine id match ayithe bill generate chesam, lekapothe "Medicine ID not found." message print cheyali, 
# and medicine quantity check chesam ante available quantity compare chesam, lekapothe "Insufficient stock" message print cheyali, and medicine price calculate chesam ante medicine price * quantity, and discount apply chesam ante total price - (total price * discount percentage / 100), and medicine quantity update chesam ante available quantity - purchased quantity,
# and bill print chesam ante medicine name, quantity, price, total price, and grand total calculate chesam ante sum of all total prices.
# discount ne float ke endhuku tisukonam ante user enter chesina discount percentage decimal value lo untundhi, and quantity ne int ke endhuku tisukonam ante user enter chesina quantity integer value lo untundhi.

    for medicine in medicines:
        if medicine["id"] == medicine_id:
            if medicine["quantity"] >= quantity:
                total_price = medicine["price"] * quantity
                total_price -= total_price * (discount_percentage / 100)
                generated_bill.append({
                    "medicine_id": medicine_id,
                    "medicine_name": medicine["name"],
                    "quantity": quantity,
                    "total_price": total_price,
                    "discount_percentage": discount_percentage
                })

# ekkada medicines counting and discount and all othet kosam ekkada store and print cheyataniki use chestam and also 
# medicine quantity update chesam ante available quantity - purchased quantity, and bill print chesam ante medicine name, quantity, price, total price, 
# and grand total calculate chesam ante sum of all total prices.



                medicine["quantity"] -= quantity
                print(f"Added {quantity} of {medicine['name']} to the bill. discount: {discount_percentage}%")
            else:
                print(f"Insufficient stock for {medicine['name']}. Available: {medicine['quantity']}discount: {discount_percentage}%")
            break
    else:
        print("Medicine ID not found.")


# ekkada nuchi emo for loop use chesam ante user enter chesina medicines count varaku repeat chesam, and medicine id, quantity, discount percentage input tisukoni bill generate chesam.
    # insuficenet inapud manaki chupistundhi infusificent ani 

        print("\n")
print(f"Customer Bill - {customer_name}")
print("-" * 40)

print("Medicine\tQty\tPrice\tTotal")

grand_total = 0


# ekkada emo medicine original price find cheyadaniki for loop use chesam ante generated_bill list lo prathi item ki medicines list lo match chesam, 
# and medicine price print chesam, and grand total calculate chesam ante sum of all total prices.


for item in generated_bill:

    # medicine original price find cheyadaniki
    for medicine in medicines:
        if medicine["id"] == item["medicine_id"]:
            price = medicine["price"]
            break

    print(
        f"{item['medicine_name']}\t"
        f"{item['quantity']}\t"
        f"₹{price}\t"
        f"₹{item['total_price']:.0f}"
    )

# ekkada emo item["total_price"] ne float ke endhuku convert chesam ante total price decimal value lo untundhi, and grand total calculate /chesam ante sum of all total prices.
# apudu ekkada nuchi table print avataniki use itundhi and also total price and grand total calculate chesam ante sum of all total prices.

    grand_total += item["total_price"]

print("-" * 40)
print(f"Grand Total: ₹{grand_total:.0f}")
print("Sale recorded successfully!")


# ekkada emo grand total print chesam ante sum of all total prices, and sale recorded successfully message print chesam ante bill generate ayyaka message ivvali.
# grand_total:.0f ante grand total decimal value lo untundhi, and .0f use chesam ante decimal value round chesam, and ₹ symbol use chesam ante currency symbol ivvali.


# Enter Customer Name: Rajani
# Enter Customer Contact: 9440355393
# Enter Case (e.g., Regular, Emergency): Emergency
# Enter number of medicines to purchase: 2
# Enter Medicine ID: m101
# Enter Quantity: 15
# Medicine ID not found.
# Enter Medicine ID: M102
# Enter Quantity: 12
# Added 12 of Ibuprofen to the bill.



# Enter Customer Name: rakesh
# Enter Customer Contact: 9440355393
# Enter Discount Percentage: 10
# Enter Case (e.g., Regular, Emergency): regular
# Enter number of medicines to purchase: 100
# Enter Medicine ID: M103
# Enter Quantity: 12
# Enter Discount Percentage for this medicine: 10
# Added 12 of Amoxicillin to the bill. discount: 10.0%
# # Enter Medicine ID: 




# Enter Customer Name: Rajani
# Enter Customer Contact: 9440355393
# Enter Discount Percentage: 10
# Enter Case (e.g., Regular, Emergency): regular
# Enter number of medicines to purchase: 2
# Enter Medicine ID: M103
# Enter Quantity: 12
# Enter Discount Percentage for this medicine: 5
# Added 12 of Amoxicillin to the bill. discount: 5.0%
# Enter Medicine ID: M105
# Enter Quantity: 12
# Enter Discount Percentage for this medicine: 5
# Added 12 of Metformin to the bill. discount: 5.0%
# Customer Bill - Rajani
# ----------------------------------------
# Medicine        Qty     Price   Total
# Amoxicillin     12      ₹20     ₹228
# Metformin       12      ₹25     ₹285
# ----------------------------------------
# Grand Total: ₹513
# Sale recorded successfully!
# PS D:\Ramansoft answers\vscode daywise\Day-1.py> 



# Enter Customer Name: Rakesh
# Enter Customer Contact: 9849658170
# Enter Discount Percentage: 20
# Enter Case (e.g., Regular, Emergency): emergency
# Enter number of medicines to purchase: 1
# Enter Medicine ID: M101
# Enter Quantity: 15
# Enter Discount Percentage for this medicine: 12
# Added 15 of Paracetamol to the bill. discount: 12.0%
# Customer Bill - Rakesh
# ----------------------------------------
# Medicine        Qty     Price   Total
# Paracetamol     15      ₹10     ₹132
# ----------------------------------------
# Grand Total: ₹132
# Sale recorded successfully!
# PS D:\Ramansoft answers\vscode daywise\Day-1.py> 