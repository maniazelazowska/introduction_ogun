print("Welcome to Papa's Pizzeria!")
price = 0
order = " "
sauce = input("Which sauce do you prefer - [T]omato or [M]ayonnaise?: ")
if sauce == "T":
    price+=12
    order+="Tomato sauce"
elif sauce == "M":
    price+=15
    order+="Mayonaisse sauce"
else:
    print("Sorry, I don't understand. Please try once again.")
    exit(13)
    
onions = input("Do you want onions? [Y/N]: ")
if onions == "Y":
    price += 4
    order += ", onions"
elif onions != "N":
    print("Sorry, I don't understand. Please try once again.")
    exit(13)

mushrooms = input("Do you want mushrooms? [Y/N]: ")
if mushrooms == "Y":
    price += 6
    order += ", mushrooms"
elif mushrooms != "N":
    print("Sorry, I don't understand. Please try once again.")
    exit(13)

garlic = input("Do you want garlic? [Y/N]: ")
if garlic == "Y":
    price += 5
    order += ", garlic"
elif garlic != "N":
    print("Sorry, I don't understand. Please try once again.")
    exit(13)  
#print("The price in total is " + str(price))
print(f"You ordered a pizza with: {order}")
print(f"The price in total is {price}")
print("Thank you, and come again! :)")

#function for asking different ingridients - homework eq. new 10 ingridients using just 10 invocations of the function