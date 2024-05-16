takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]
delivery_fee = 5.00
free_delivery_price = 30.00
print("Welcome to the takeaway delivery service.")
print("Here's our menu.")
for item in takeaway_menu:
    print(item)
    

name = input('Enter your name: ')
quantity = int(input("How many items would you like to purchase?: "))
order = []
price = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
    

print(f"Thank you {name}, your order is as follows:")
for item in order:
    print(takeaway_menu[item-1])
    price.append(takeaway_prices[item-1])
    
def get_bill_total(price):
    value = sum(price)
    if value < 30:
        value += delivery_fee
    return round(value, 2)

print(f"Your total comes to {get_bill_total(price)} euros")

