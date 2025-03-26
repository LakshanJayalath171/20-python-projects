# Python banking program

def show_balance(balance):
    print(f"Your Balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter Your Amount: "))

    if(amount<0):
        print("Deposite value must be a Positive number:")
        return 0
    else:
        return amount

def withdraw(balance):

    amount = float(input('Enter your Amount: '))

    if(amount<0):
        print("Amount Must Be a Positive!")
        return 0
    elif(balance<amount):
        print("Your Account Balance is insufficient")
        return 0

    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program__")
        print("01.Show balance ")
        print("02.Deposit")
        print("03.Withdraw")
        print("04.Exit")

        u_choice = input("Enter Your Choice: ")

        if (u_choice == "1"):
            show_balance(balance)
        elif (u_choice == "2"):
            balance += deposit()

        elif (u_choice == "3"):
            balance -= withdraw(balance)

        elif (u_choice == "4"):
            is_running = False
        else:
            print("Make A Valid Choice")

    print("Thank You.have A nice day ")

if __name__ == '__main__':
    main()

