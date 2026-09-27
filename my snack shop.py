
snack_name = "Potato Chips"   
price = 1.75                 
quantity = 12                 
is_available = True          

print("--- Step 2: Snack Details and Types ---")
print("Snack Name:", snack_name, "| Type:", type(snack_name))
print("Price:", price, "| Type:", type(price))
print("Quantity:", quantity, "| Type:", type(quantity))
print("Is Available:", is_available, "| Type:", type(is_available))
print()

total_stock_value = price * quantity
sale_price = price * 0.80  
double_stock = quantity * 2

print("--- Step 3: Arithmetic Calculations ---")
print("Total Stock Value: $", total_stock_value)
print("Sale Price (20% off): $", sale_price)
print("Double Stock Quantity:", double_stock)
print()

is_under_two = price < 2.00
is_quantity_greater_than_five = quantity > 5
is_exactly_one_fifty = price == 1.50

print("--- Step 4: Comparison Checks ---")
print("Is the price under $2.00?:", is_under_two)
print("Is the quantity greater than 5?:", is_quantity_greater_than_five)
print("Is the price exactly $1.50?:", is_exactly_one_fifty)
print()


shop_name = "Quick" + " " + "Bites"
name_length = len(snack_name)
first_letter = snack_name[0]

print("--- Step 5: String Operations ---")
print("Shop Name:", shop_name)
print("Number of letters in snack name:", name_length)
print("First letter of snack name:", first_letter)
print()

price_a = 2.50
price_b = 0.99

print("--- Step 6: Swapping Variables ---")
print("Before swap -> Price A:", price_a, "| Price B:", price_b)


temp = price_a
price_a = price_b
price_b = temp

print("After swap  -> Price A:", price_a, "| Price B:", price_b)







