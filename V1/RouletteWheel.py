import random

colors = ['Green', "Green", 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Black',]

def bet():
    try:
        betvar = int(input("Enter your bet: "))
        if betvar < 0:
            print("Invalid bet. Please enter a positive number.")
            bet()
        else:
            inpcolor = input("Please enter a color (r/b): ")
            if inpcolor.lower()!= 'r' and inpcolor.lower()!= 'b':
                print("Invalid color. Please enter 'r' or 'b'.")
                bet()
            else: getnum(betvar, inpcolor)
    except ValueError:
        print("Invalid bet. Please enter a valid number.")
        bet()

def getnum(bet, color):
    col = random.choice(colors)
    print(f"The ball landed on {col}.")
    if col == "Green":
        print("You lost you money, money goes to house.")
        print()
        playagain()
    elif col[0].lower() == color.lower():
        print(f"Congratulations! You won {bet*2}!")
        playagain()
    else:
        print(f"Sorry, you lost your bet. Your money goes to house.")
        playagain()

def playagain():
    again = input("Do you want to play again? (y/n): ").lower()
    if again.lower() == 'y': bet()
    else:
        print("Thank you for playing!")
        quit()

bet()