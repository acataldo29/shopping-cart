
#Create list Products
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] 

#User-defined Functions
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

def countX(x): #matching_products[i]["id"]
    """
    This function returns a list of individual item count to use on 
    the receipt. 

    This function is used in a for loop with the input matching the 
    comment next to the def statement
    """
    count = 1
    for i in matching_product_id:
        if int(i) == x:
            count = count + 1
            countlist.append(count)

################################################ Begin User Code ################################################

# 1) Load/Import packages
import os
import operator
from datetime import datetime
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient


# 2) Allow clerk to input id
matching_product_id = []
while True:
    p_input = input(f"Please input the Product ID (1 to {len(products)} are valid), or 'Done' if there are no more items: ")
    if p_input == "Done":
        print("SHOPPING CART ITEM ID(S):", matching_product_id)
        print("--------------------------------------")
        print("GENERATING RECEIPT...")
        break
    elif int(p_input) in range(1, len(products)+1):
        matching_product_id.append(p_input)
    else:
        print("PRODUCT ID is invalid, please try again!")

print("--------------------------------------")

# 4) Generate Receipt based on Product inputs
print("ANTHONY'S AMAZING ASSEMBLY OF GROCERIES")
print("WWW.ANTGROCERIES.COM")
print("--------------------------------------")

today = datetime.now()
today = today.strftime("%Y-%m-%d %I:%M %p")
print(f"CHECKOUT AT:", today)

print("--------------------------------------")

        #List Products
print("SELECTED PRODUCTS:")

matching_products = []
for item in products:
    if str(item["id"]) in matching_product_id:
        matching_products.append(item)

no_dup = []
no_dup = [x for x in matching_products if x["id"] not in no_dup]

frequency = []
for i in matching_product_id:
   for j in range(1, len(matching_product_id)):
        if i in frequency:
            frequency += 1
        else:
            frequency = 1


#count = operator.getitem(frequency.values()[2], frequency)
#print(count)

for j in range(1, len(no_dup)):
    print(f"{count[j]}x...", no_dup[j]["name"], "("+str(no_dup[j]["price"])+")")