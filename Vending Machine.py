print("HELLO AND WELCOME TO THE ZOMDER MART!")
print("Zomder Mart was founded by: Errol Renselle B. Caranza, or known by his alias online: Zomder")

print("=====================================")
print("List of Snacks:")
print("Code = 11 : 7 Days Crossiant Chocolate = 3 AED")
print("Code = 12 : 7 Days Crossiant Strawberry = 3 AED")
print("Code = 13 : 7 Days Crossiant Caramel = 3 AED")
print("Code = 14 : L'sine Muffin Chocolate = 3 AED")
print("Code = 15 : L'sine Muffin Blueberry = 3 AED")
print("Code = 16 : L'sine Muffin Red Velvet = 3 AED")
print("Code = 17 : Oreo Original Flavor 10pcs = 5 AED")
print("Code = 18 : Oreo Chocolate Flavor 10pcs = 5 AED")
print("Code = 19 : M&Ms Chocolate = 3 AED")
print("Code = 20 : M&Ms Peanut = 3 AED ")
print("Code = 21 : Toblerone Milk Chocolate = 9 AED")
print("Code = 22 : Toblerone White Chocolate = 9 AED")
print("Code = 23 : Toblerone Dark Chocolate = 9 AED")
print("Code = 24 : Zomder Chocolate = 10 AED")
print("=====================================")
        
snack_choice = int(input("Please select a snack. If none, press 0: "))

if snack_choice == 11:
  snack = "7 Days Crossiant Chocolate"
  print("You have selected an item:", snack,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")
      
elif snack_choice == 12:
  snack = "7 Days Crossiant Strawberry"
  print("You have selected an item:", snack,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 13:
  snack = "7 Days Crossiant Caramel"
  print("You have selected an item:", snack,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 14:
  snack = "L'sine Muffin Chocolate"
  print("You have selected an item:", snack,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 15:
  snack = "L'sine Muffin Blueberry"
  print("You have selected an item:", snack,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 16:
  snack = "L'sine Muffin Red Velvet"
  print("You have selected an item:", snack,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 17:
  snack = "Oreo Original Flavor 10pcs"
  print("You have selected an item:", snack,)
  print("Cost: 6 AED")
  price = 6
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 18:
  snack = "Oreo Chocolate Flavor 10pcs"
  print("You have selected an item:", snack,)
  print("Cost: 6 AED")
  price = 6
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 19:
  snack = "M&Ms Chocolate"
  print("You have selected an item:", snack,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 20:
  snack = "M&Ms Chocolate With Nuts"
  print("You have selected an item:", snack,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 21:
  snack = "Toblerone Milk Chocolate"
  print("You have selected an item:", snack,)
  print("Cost: 9 AED")
  price = 9
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 22:
  snack = "Toblerone White Chocolate"
  print("You have selected an item:", snack,)
  print("Cost: 9 AED")
  price = 9
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 23:
  snack = "Toblerone Dark Chocolate"
  print("You have selected an item:", snack,)
  print("Cost: 9 AED")
  price = 9
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 24:
  snack = "Zomder Chocolate"
  print("You have selected an item:", snack,)
  print("Cost: 10 AED")
  price = 10
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", snack, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", snack, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif snack_choice == 0:
  print("Choosing Snack Had Been Skipped.")

else:
  print("You have entered an invalid code.")

print("=====================================")
print("List of Drinks:")
print("Code = 25 : Water = 1 AED")
print("Code = 26 : Pepsi = 3 AED")
print("Code = 27 : Sprite = 3 AED")
print("Code = 28 : Fanta = 3 AED")
print("Code = 29 : Mountain Dew = 3 AED")
print("Code = 30 : Nescafe Iced Coffee Latte = 6 AED")
print("Code = 31 : Nescafe Iced Coffee Caramel = 6 AED")
print("Code = 32 : Nescafe Iced Coffee Mocha = 6 AED")
print("Code = 33 : Lacnor Strawberry Milk = 2 AED")
print("Code = 34 : Lacnor Chocolate Milk = 2 AED")
print("Code = 35 : Lacnor Banana Milk = 2 AED")
print("Code = 36 : Lacnor Orange Juice = 2 AED")
print("Code = 37 : Lacnor Mango Juice = 2 AED")
print("Code = 38 : Lacnor Cranberry Juice = 2 AED")
print("Code = 39 : Lacnor Apple Juice = 2 AED")
print("Code = 40 : Zomder Energy Drink = 11 AED")
print("=====================================")
        
drink_choice = int(input("Please select a drink. If none, press 0: "))
          
if drink_choice == 25:
  drink = "Water"
  print("You have selected an item:", drink,)
  print("Cost: 1 AED")
  price = 1
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 26:
  drink = "Pepsi"
  print("You have selected an item:", drink,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had been dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 27:
  drink = "Sprite"
  print("You have selected an item:", drink,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 28:
  drink = "Fanta"
  print("You have selected an item:", drink,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 29:
  drink = "Mountain Dew"
  print("You have selected an item:", drink,)
  print("Cost: 3 AED")
  price = 3
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("received a change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 30:
  drink = "Nescafe Iced Coffee Latte"
  print("You have selected an item:", drink,)
  print("Cost: 6 AED")
  price = 6
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 31:
  drink = "Nescafe Iced Coffee Caramel"
  print("You have selected an item:", drink,)
  print("Cost: 6 AED")
  price = 6
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 32:
  drink = "Nescafe Iced Coffee Mocha"
  print("You have selected an item:", drink,)
  print("Cost: 6 AED")
  price = 6
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 33:
  drink = "Lacnor Strawberry Milk"
  print("You have selected an item:", drink,)
  print("Cost: 2 AED")
  price = 2
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 34:
  drink = "Lacnor Chocolate Milk"
  print("You have selected an item:", drink,)
  print("Cost: 2 AED")
  price = 2
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 35:
  drink = "Lacor Banana Milk"
  print("You have selected an item:", drink,)
  print("Cost: 2 AED")
  price = 2
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 36:
  drink = "Lacnor Orange Juice"
  print("You have selected an item:", drink,)
  print("Cost: 2 AED")
  price = 2
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 37:
  drink = "Lacor Mango Juice"
  print("You have selected an item:", drink,)
  print("Cost: 2 AED")
  price = 2
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 38:
  drink = "Lacnor Cranberry Juice"
  print("You have selected an item:", drink,)
  print("Cost: 2 AED")
  price = 2
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")

elif drink_choice == 39:
  drink = "Lacnor Apple Juice"
  print("You have selected an item:", drink,)
  print("Cost: 2 AED")
  price = 2
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")
                
elif drink_choice == 40:
  drink = "Zomder Energy Drink"
  print("You have selected an item:", drink,)
  print("Cost: 10 AED")
  price = 10
  money_in = int(input("Insert an amount here: "))
  money_out = money_in - price
  if money_in > price:
    print("The item:", drink, ",had dispensed")
    print("Claimed item and change of", money_out, "AED")
  elif money_in == price:
    print("The item:", drink, ", had dispensed")
  else:
    print("You don't have enough money to purchase this item")
        
elif drink_choice == 0:
  print("Selecting a drink had been skipped.")

else:
  print("You have entered an invalid code.")

print("THANK YOU FOR BUYING HERE IN THE ZOMDER MART. HOPE YOU WILL COME AGAIN HERE")
print("Follow Zomder Mart:")
print("Twitter: @ZomderMart")
print("Instagram: @zomdermartsagram")
print("-------------------------------------")
print("Follow Zomder Through These Social Medias:")
print("Twitter - @Zomderleper22")
print("Instagram - @zomderstagram")