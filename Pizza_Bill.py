print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

if size == 's':
    pizza_size = 15
elif size == 'm':
    pizza_size = 20
else:
    pizza_size = 25


if add_pepperoni == 'y':
    if size == 's':
        pepperoni = pizza_size +2
    else:
        pepperoni = pizza_size +3
else:
    pepperoni = pizza_size

if extra_cheese == 'y':
   cheese = pepperoni +1
else:
    cheese = pepperoni
print(f"Total amount of bill is {cheese}")

