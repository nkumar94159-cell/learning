# Dictionary of Dictionaries: Store inventory
# Keys are product IDs, values are dictionaries containing product details
inventory = {
"T101": {"name": "Laptop", "price": 1200.00, "stock": 5},
"T102": {"name": "Wireless Mouse", "price": 25.50, "stock": 0},
"T103": {"name": "Mechanical Keyboard", "price": 85.00, "stock": 12},
"T104": {"name": "USB-C Hub", "price": 40.00, "stock": 3},
"T105": {"name": "Monitor", "price": 300.00, "stock": 2}
}
# List of strings: Tags for the store (contains duplicates)
raw_tags = ["computing", "accessories", "computing", "peripherals", "office",
"accessories"]
# List of Tuples: A customer's shopping cart.
# Format: (product_id, requested_quantity)
shopping_cart = [("T101", 1), ("T102", 1), ("T104", 4), ("T103", 2)]
# -------------------------------------------------------------

# Task 1

new_raw_tags= set(raw_tags)
print(f"Welcome users please find unique categories list {new_raw_tags}")

#Task 2

total_cost=0
out_of_stock_items=[]

for prod_id in shopping_cart:
    if prod_id[0] in inventory:
        print("Yes, Prduct exist")
    else:
        print("No Prodcut deosn't exist ")


for item in shopping_cart:
    prod_id = item[0]
    requested_quantity = item[1]
    if requested_quantity <= inventory[prod_id]['stock']:
        inventory[prod_id]['stock'] = inventory[prod_id]['stock'] - requested_quantity
        total_cost += requested_quantity *  inventory[prod_id]['price'] 
    else:
        out_of_stock_items.append(inventory[prod_id]['name'])

# Task 3
#print(f"{total_cost:.2f}")

for item in out_of_stock_items:
    print(f"Sorry for inconvence we dont these items currenlty {item} ") 
    
    
#updated inventory
for item, detail in inventory.items():
    print(f"updatee inevntory {item}, {detail['name']} , {detail['stock']}")