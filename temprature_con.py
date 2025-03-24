unit = input("Is The Temprature In Celcius Or Farenheight: ").upper()
temp = float(input("Input The Temprature: "))

if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"This Temprature in Farenheight is: {temp}F")
elif unit =="F":
    temp = round((temp-32)*5/9,1)
    print(f"This Temprature in Celcius is: {temp}F")
else:
    print(f"Invalid Unit Detected {unit}")