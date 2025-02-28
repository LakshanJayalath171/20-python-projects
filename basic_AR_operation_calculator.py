operator = input("Enter A Operator: ")
num_01 = float(input("Enter First Number: "))
num_02 = float(input("Enter Second Number: "))

if operator == "+":
    print(f'{num_01} + {num_02} = {num_01+num_02}')
elif operator == "-":
    print(f"{num_01} - {num_02} = {num_01-num_02}")
elif operator == "/":
    print(f"{num_01} / {num_02} = {num_01/num_02}")
elif operator == "%":
    print(f"{num_01} % {num_02} = {num_01%num_02}")
elif operator == "*":
    print(f'{num_01} * {num_02} = {num_01*num_02}')
else:
    print("Make A Valid Operator '+,-,/,*,%'")
