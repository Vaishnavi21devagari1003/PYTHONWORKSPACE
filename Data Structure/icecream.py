
 
flavors = ("Vanilla", "Chocolate", "Strawberry")
 
# Prices
prices = {
    "Vanilla": 80,
    "Chocolate": 90,
    "Strawberry": 85
}
 
# Allowed serving types
servings = frozenset({"Cone", "Cup"})
 
# Order history
orders = []
 
print("Welcome to Scoops & Scripts")
 
# Take input
flavor = input("Enter flavor: ").title()
 
if flavor in flavors:
    serving = input("Enter serving (Cone/Cup): ").title()
 
    if serving in servings:
        toppings_input = input("Enter toppings (comma separated): ")
 
        if toppings_input == "":
            toppings = set()
        else:
            toppings = set(toppings_input.split(","))
 
        price = prices[flavor]
 
        order = {
            "Flavor": flavor,
            "Serving": serving,
            "Toppings": toppings,
            "Price": price
        }
 
        orders.append(order)
 
        print("Order placed successfully")
        print(order)
    else:
        print("Invalid serving type")
else:
    print("Invalid flavor")