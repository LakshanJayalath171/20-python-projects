weight = int(input("Enter A Weight: "))
unit = input("Kilogram Or Pounds: (K or L)")

if unit=="L":
    weight = weight * 2.205
    printing_unit = "Lbs."
    print(f"Your weight is {weight} {printing_unit}")
elif unit =="K":
    weight = weight/2.205
    printing_unit = "kgs."
    print(f"Your weight is {weight} {printing_unit}")
else:
    print(f"{unit} Was not valid")

