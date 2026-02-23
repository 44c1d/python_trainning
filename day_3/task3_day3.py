#Build an automatic pizza program. 
# Based on user´s order, work out their final bill. Use the input() function to get a user´s
#preferences and then add up the total for their order and tell them hoy much they have to pay.
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza(L): $25
#Add pepperoni : $2 
#Add Extra cheese : $2

pizza_size = input("Hello! Welcome to the Python Pizza's. What size of pizza wnat to order? S ,M or L ").upper()

if pizza_size == "S":
    bill = 15
elif pizza_size == "M":
    bill = 20
elif pizza_size =="L":
    bill = 25

pepperoni = input("Do you want to add Pepperoni?($2 extra) Y or N ").upper()
if pepperoni =="Y":
    bill+2
extra_cheese = input("Do you want to add extra cheese? ($2 extra) Y or N ").upper()
if extra_cheese =="Y":
    bill+2
      

print(f"Total amount: ${bill}")







