foods = []
pricess = []

total = 0

while True:

    choose = input("Enter A Name You Want Buy ('Q' for quit): ")
    upper_choose = choose.upper()
    if(upper_choose=="Q" ):
        break
    else:
        price = float(input(f"Enter A Price Of {choose} $"))
        foods.append(choose)
        pricess.append(price)

print("-----YOUR CART------")

for food in foods:
    print(food, end=" ")

for price in  pricess:
    total +=price

print(f"Your Total is {total}")