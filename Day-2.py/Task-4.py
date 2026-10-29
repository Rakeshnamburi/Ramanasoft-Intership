 #E-commerce Order Processing System Problem  



# Statement:  
# You are working for an e-commerce company that processes customer orders. Each order contains 
# product information stored as tuples in the format: (product_id, product_name, price, quantity). You 
# need to process multiple orders and generate various reports. 


orders = [  

[ (101, "Laptop", 999.99, 1),  
(102, "Mouse", 25.50, 2),  
(103, "Keyboard", 75.00, 1) ],  
[ (101, "Laptop", 999.99, 2),  
(104, "Monitor", 299.99, 1),  
(105, "Webcam", 89.99, 1) ],  
[ (102, "Mouse", 25.50, 3),  
(103, "Keyboard", 75.00, 2),  
(106, "Headphones", 199.99, 1)]  
]
threshold_value = 1000.00 



# 1. Calculate the total value of each order 

for i, order in enumerate(orders, start=1):
    total_value = sum(item[2] * item[3] for item in order)
    print(f"Total value of Order {i}: ${total_value:.2f}")

# ekkada use chesina technique enti ante prathi order lo product price and quantity ni multiply chesi total value calculate chesthundi. 
# sum() function use chesi prathi order lo total value calculate chesthundi.
# remeaning order lo product price and quantity ni multiply chesi total value calculate chesthundi.


# 2. Find the most expensive single item across all orders  

largest_item = max((item for order in orders for item in order), key=lambda x: x[2])
print(f"\nMost expensive single item: {largest_item[1]} (Product ID: {largest_item[0]}) - Price: ${largest_item[2]:.2f}")


# f"\n enkada use chesina technique enti ante prathi order lo product price ni compare chesi maximum price unna item ni find chesthundi."
# largest item ante prathi order lo product price ni compare chesi



# 3. Create a summary of total quantities sold for each product  

from collections import defaultdict

product_quantities = defaultdict(int)
for order in orders:
    for item in order:
        product_quantities[item[0]] += item[3]

for product_id, total_quantity in product_quantities.items():
    print(f"Product ID: {product_id} - Total Quantity Sold: {total_quantity}")


# ekkada use chesina technique enti ante defaultdict use chesi prathi product id ki total quantity sold calculate chesthundi.


# 4. Identify orders that exceed a certain value threshold  

exceeding_orders = []
for i, order in enumerate(orders, start=1):
    total_value = sum(item[2] * item[3] for item in order)
    if total_value > threshold_value:
        exceeding_orders.append((i, total_value))   

for order_num, total in exceeding_orders:
    print(f"Order {order_num} exceeds the threshold with a total value of ${total:.2f}")


# ekkada use chesina technique enti ante prathi order lo product price and quantity ni multiply chesi total value calculate chesthundi.
# if total value threshold value kanna ekkuva unte, exceeding_orders list lo append chesthundi. Finally, exceeding orders ni print chesthundi.  

# 5. Generate a list of unique products ordered

unique_products = set()
for order in orders:
    for item in order:
        unique_products.add((item[0], item[1]))  # Add product_id and product_name as a tuple
for product_id, product_name in unique_products:
    print(f"Product ID: {product_id}, Product Name: {product_name}")


# ekkada use chesina technique enti ante set() use chesi prathi order lo unique product id and product name ni add chesthundi. Finally, unique products ni print chesthundi.    

