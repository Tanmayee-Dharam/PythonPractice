'''
Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

'''

print("Thank you for choosing Python Pizza Delivery!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input(" Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Multiple conditions hence we can opt for multiple ifs

# Check size
if size == 'S':
    price = 15

elif size == "M":
    price = 20

else:
    price = 25

# Check if customer wants pepperoni
if add_pepperoni == "Y":
    if size == "S":
        price = price + 2
    else:
        price = price + 3
else:
    price = price

# Check if customer want extra cheese
if extra_cheese == "Y":
    price = price + 1

else:
    price = price

print(f"Your final bill is: ${price}.")









