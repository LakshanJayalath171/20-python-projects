# slot machine program
import random
import time

def spin_row():

    symbols = ['🍒','🍉' , '🍋', '🔔' ,'⭐']

    choices = []

    for symbol in range(3):
        choices.append(random.choice(symbols))

    return choices

def print_row(row):
    print('**************')
    print(" | ".join(row))
    print('**************')

def get_payout(row,bet):

    if row[0] == row[1] == row[2]:

        if row[0] == "🍒":
            return bet*3
        elif row[0] == "🍉":
            return bet*5
        elif row[0]=="🍋":
            return bet*7
        elif row[0]=="🔔":
            return bet*10
        elif row[0]=="⭐":
            return bet*15
    else:
        return 0

def main():

    balance = 100

    print("***********************")
    print("Wellcome to python slot")

    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***********************")

    while balance>0:
        print(f"Current balance is : {balance}$")
        bet = input("Enter Amount Of Bet: ")

        if not bet.isdigit():
            print('Please Enter A Valid Number: ')
            continue

        bet = int(bet)

        if balance<bet:
            print("Insufficient Balance")
            continue

        if bet <=0:
            print("Bet must be a greater than 0")

        balance -=bet

        row = spin_row()
        print("spinning.")
        time.sleep(0.5)
        print("spinning..")
        time.sleep(0.5)
        print("spinning...")
        print_row(row)

        payout = get_payout(row,bet)

        if payout>0:
            print(f'You won ${payout}')
        else:
            print("Sorry You Lose")

        balance +=payout

        play_again = input("Are You Want To Play Again (Y/N): ").upper()

        if not play_again == "Y":
            break

print("****************")
print("Game Over")
print("****************")

if __name__ == '__main__':
    main()
