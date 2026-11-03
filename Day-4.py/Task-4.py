# 4. Pharmacy Inventory System – Billing Feature: 

medicines = [
    {"id": "M101", "name": "Paracetamol", "price": 10, "quantity": 100},
    {"id": "M102", "name": "Ibuprofen", "price": 15, "quantity": 50},
    {"id": "M103", "name": "Amoxicillin", "price": 20, "quantity": 30},
    {"id": "M104", "name": "Cetirizine", "price": 12, "quantity": 80},
    {"id": "M105", "name": "Metformin", "price": 25, "quantity": 40}
]

generated_bill = []
customer_name = input("Enter Customer Name: ")
customer_contact = input("Enter Customer Contact: ")
case = input("Enter Case (e.g., Regular, Emergency): ")
count = int(input("Enter number of medicines to purchase: "))

for _ in range(count):
    medicine_id = input("Enter Medicine ID: ")
    quantity = int(input("Enter Quantity: "))

    for medicine in medicines:
        if medicine["id"] == medicine_id:
            if medicine["quantity"] >= quantity:
                total_price = medicine["price"] * quantity
                generated_bill.append({
                    "medicine_id": medicine_id,
                    "medicine_name": medicine["name"],
                    "quantity": quantity,
                    "total_price": total_price
                })
                medicine["quantity"] -= quantity
                print(f"Added {quantity} of {medicine['name']} to the bill.")
            else:
                print(f"Insufficient stock for {medicine['name']}. Available: {medicine['quantity']}")
            break
    else:
        print("Medicine ID not found.")
