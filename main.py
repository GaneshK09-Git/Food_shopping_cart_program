#Exercise 12: Food shopping cart program
#we can replace food/foods with item/items to use it for general purpose shopping



foods = []
prices = []
total = 0


while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q': #lower() means can use Q or q
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food, end =" ")

for price in prices:
    total +=price

print() #new line
print(f"Your total is: ${total}")
