# Dictionary of Dictionaries: Store inventory
# Keys are product IDs, values are dictionaries containing product details
inventory = {
"T101": {"name": "Laptop", "price": 1200.00, "stock": 5},
"T102": {"name": "Wireless Mouse", "price": 25.50, "stock": 0},
"T103": {"name": "Mechanical Keyboard", "price": 85.00, "stock": 12},
"T104": {"name": "USB-C Hub", "price": 40.00, "stock": 3},
"T105": {"name": "Monitor", "price": 300.00, "stock": 2}
}

#print(inventory['T101']['name'], inventory['T101']['stock'])

# List of strings: Tags for the store (contains duplicates)
raw_tags = ["computing", "accessories", "computing", "peripherals", "office",
"accessories"]

new_raw_tags= set(raw_tags)
print(new_raw_tags)

# List of Tuples: A customer's shopping cart.
# Format: (product_id, requested_quantity)
shopping_cart = [("T101", 1), ("T102", 1), ("T104", 4), ("T103", 2)]

#print(shopping_cart[0][1])

#Task 1
#print(f"Welcome the store {new_raw_tags}")

#Task 2:
total_cost = 0
out_of_stock_items =[]

#Check if the requested product ID exists in the inventory.
for product_id in shopping_cart:
    if product_id[0] in inventory:
        print(f"yes, Product {product_id[0]} is exist in the inventory")
    else:
        print(f"No, Product {product_id}[0] is not exist in the inventory")

#print(shopping_cart) 
#print (inventory['T101']['stock'])   
# 2 Check if there is enough stock to fulfill the requested_quantity.

for item in shopping_cart:
    product = item[0]
    requested_quantity =item[1]
    #print(f"Final Total Cost: ${total_cost:.2f}")
    #print(product, requested_quantity)

    if requested_quantity <= inventory[product]['stock']:
        inventory[product]['stock'] = inventory[product]['stock'] - requested_quantity
        total_cost +=  requested_quantity *  inventory[product]['price'] 
        #print(total_cost)
    else:
        product_name = inventory[product]['name']
        out_of_stock_items.append(product_name)
        #print(out_of_stock_items)
        
print(f"Final Total Cost: ${total_cost:.2f}")
print(f"Sorry for your incovenince we dont have current item in stock  {out_of_stock_items}")
print("\n--- Updated Master Inventory ---")
for prod_id, details in inventory.items():
    print(f"Product ID: {prod_id} , Name: {details['name']} , Remaining Stock: {details['stock']}")






    




