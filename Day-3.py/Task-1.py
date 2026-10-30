# Task 1: E-commerce Product Inventory Manager


# Sample Input:

products = [  
    "iPhone14:Electronics:89999:15",
    "Samsung_TV:Electronics:45000:0",  
    "Nike_Shoes:Fashion:8999:25",  
    "Adidas_Shirt:Fashion:2999:10",  
    "MacBook:Electronics:129999:5",  
    "Levi_Jeans:Fashion:4999:0",  
    "iPad:Electronics:35999:12"  
]

# 1. Create a dictionary to store product information  


products_list = []
for product in products:
    product_data = product.split(":")
    product_dict = {
        "name": product_data[0],
        "category": product_data[1],
        "price": int(product_data[2]),
        "stock": int(product_data[3])
    }
    products_list.append(product_dict)
    print(f"Product Name: {product_dict['name']}, Category: {product_dict['category']}, Price: {product_dict['price']}, Stock: {product_dict['stock']}")






    # 2. Find the most expensive product in each category 

    products_by_category = {}
for product in products_list:
    category = product["category"]
    if category not in products_by_category:
        products_by_category[category] = product
    else:
        if product["price"] > products_by_category[category]["price"]:
            products_by_category[category] = product

            print(f"Most Expensive Product in {category}: {product['name']}, Price: {product['price']}")






    # 3. Identify products that are out of stock (stock = 0)  

out_of_stock_products = []
for product in products_list:
    if product["stock"] == 0:
        out_of_stock_products.append(product)

        print(f"Out of Stock Product: {product['name']}, Category: {product['category']}, Price: {product['price']}")   






# 4. Calculate total inventory value by category 

total_inventory_value_by_category = {}
for product in products_list:
    category = product["category"]
    if category not in total_inventory_value_by_category:
        total_inventory_value_by_category[category] = 0
    total_inventory_value_by_category[category] += product["price"] * product["stock"]


print("Most Expensive Products by Category:")
for category, product in products_by_category.items():
    print(f"Category: {category}, Product: {product['name']}, Price: {product['price']}")
    print(f"Total Inventory Value for {category}: {total_inventory_value_by_category[category]}")
