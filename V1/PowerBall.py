import random
from time import sleep

def askbet():
    global bet
    try:
        bet = int(input("\nEnter your bet: "))
        ask(bet)
    except ValueError:
        print("Please enter a valid bet")
        askbet()

def ask(bet):
    try:
        n1, n2, n3, n4, n5, n6 = int(input("Enter your 1st number (1-69): ")), int(input("Enter your 2nd number (1-69): ")), int(input("Enter your 3rd number (1-69): ")), int(input("Enter your 4th number (1-69): ")), int(input("Enter your 5th number (1-69): ")), int(input("Enter the red number (1-26): ")) 
        if n1 > 69 or n1 < 1 or n2 > 69 or n2 < 1 or n3 > 69 or n3 < 1  or n4 > 69 or n4 < 1 or n5 > 69 or n5 < 1 or n6 > 26 or n6 < 1:
            print("Please enter a valid number\n")
            ask(bet)
        else:
            print('Running numbers...\n')
            sleep(3)
            see_if_won(bet, n1, n2, n3, n4, n5, n6)
    except ValueError:
        print("Please enter a valid number\n")
        ask(bet)
        
def see_if_won(bet, n1, n2, n3, n4, n5, n6):
    rn1, rn2, rn3, rn4, rn5, rn6 = random.randint(1,69), random.randint(1,69), random.randint(1,69), random.randint(1,69), random.randint(1,69), random.randint(1,26)
    print(f"The numbers are:  {rn1} {rn2} {rn3} {rn4} {rn5} | {rn6}")
    print(f"Your numbers are: {n1} {n2} {n3} {n4} {n5} | {n6}")
    
    if rn6 == n6:
        if rn1 == n1 and rn2 == n2 and rn3 == n3 and rn4 == n4 and rn5 == n5:
            print(f"You guessed all the numbers correctly!\nYou won: ${bet*100}!")
            play_again()
        elif (rn1 == n1 and rn2 == n2 and rn3 == n3 and rn4 == n4) or (rn2 == n2 and rn3 == n3 and rn4 == rn4 and rn5 == n5) or (rn1 == n1 and rn3 == n3 and rn4 == n4 and rn5 == n5) or (rn1 == n1 and rn2 == n2 and rn4 == n4 and rn5 == n5) or (rn1 == n1 and rn2 == n2 and rn3 == n3 and rn5 == n4):
            print(f"You guessed 5/6 numbers correctly!\nYou won: ${bet*64}!")
            play_again()
        elif (rn1 == n1 and rn2 == n2 and rn3 == n3) or (rn1 == n1 and rn2 == n2 and rn5 == n5) or (rn1 == n1 and rn4 == n4 and rn5 == n5) or (rn3 == n3 and rn4 == n4 and rn5 == n5) or (rn2 == n2 and rn4 == n4 and rn5 == n5) or (rn2 == n2 and rn3 == n3 and rn5 == n5) or (rn2 == n2 and rn3 == n3 and rn4 == n4) or (rn1 == n1 and rn3 == n3 and rn5 == n5) or (rn1 == n1 and rn3 == n3 and rn4 == n4) or (rn1 == n1 and rn2 == n2 and rn4 == n4):
            print(f"You guessed 4/6 numbers correctly!\nYou won: ${bet*32}!")
            play_again()
        elif (rn1 == n1 and rn2 == n2) or (rn1 == n1 and rn3 == n3) or (rn1 == n1 and rn4 == n4) or (rn1 == n1 and rn5 == n5) or (rn2 == n2 and rn3 == n3) or (rn2 == n2 and rn4 == n4) or (rn2 == n2 and rn5 == n5) or (rn3 == n3 and rn4 == n4) or (rn3 == n3 and rn5 == n5) or (rn4 == n4 and rn5 == n5):
            print(f"You guessed 3/6 numbers correctly!\nYou won: ${bet*16}!")
            play_again()
        elif rn1 == n1 or rn2 == n2 or rn3 == n3 or rn4 == n4 or rn5 == n5:
            print(f"You guessed 2/6 number correctly!\nYou won: ${bet*8}!")
            play_again()
        else:
            print(f"You guessed the red number correctly!\nYou won: ${bet*5}!")
            play_again()
        
    else:
        if rn1 == n1 and rn2 == n2 and rn3 == n3 and rn4 == n4 and rn5 == n5:
            print(f"You guessed 5/6 numbers correctly!\nYou won: ${bet*64}!")
            play_again()
        elif (rn1 == n1 and rn2 == n2 and rn3 == n3 and rn4 == n4) or (rn2 == n2 and rn3 == n3 and rn4 == rn4 and rn5 == n5) or (rn1 == n1 and rn3 == n3 and rn4 == n4 and rn5 == n5) or (rn1 == n1 and rn2 == n2 and rn4 == n4 and rn5 == n5) or (rn1 == n1 and rn2 == n2 and rn3 == n3 and rn5 == n4):
            print(f"You guessed 4/6 numbers correctly!\nYou won: ${bet*32}!")
            play_again()
        elif (rn1 == n1 and rn2 == n2 and rn3 == n3) or (rn1 == n1 and rn2 == n2 and rn5 == n5) or (rn1 == n1 and rn4 == n4 and rn5 == n5) or (rn3 == n3 and rn4 == n4 and rn5 == n5) or (rn2 == n2 and rn4 == n4 and rn5 == n5) or (rn2 == n2 and rn3 == n3 and rn5 == n5) or (rn2 == n2 and rn3 == n3 and rn4 == n4) or (rn1 == n1 and rn3 == n3 and rn5 == n5) or (rn1 == n1 and rn3 == n3 and rn4 == n4) or (rn1 == n1 and rn2 == n2 and rn4 == n4):
            print(f"You guessed 3/6 numbers correctly!\nYou won: ${bet*16}!")
            play_again()
        elif (rn1 == n1 and rn2 == n2) or (rn1 == n1 and rn3 == n3) or (rn1 == n1 and rn4 == n4) or (rn1 == n1 and rn5 == n5) or (rn2 == n2 and rn3 == n3) or (rn2 == n2 and rn4 == n4) or (rn2 == n2 and rn5 == n5) or (rn3 == n3 and rn4 == n4) or (rn3 == n3 and rn5 == n5) or (rn4 == n4 and rn5 == n5):
            print(f"You guessed 2/6 numbers correctly!\nYou won: ${bet*8}!")
            play_again()
        elif rn1 == n1 or rn2 == n2 or rn3 == n3 or rn4 == n4 or rn5 == n5:
            print(f"You guessed 1/6 number correctly!\nYou won: ${bet*4}!")
            play_again()
        else:
            print(f"Sorry, you didn't guess any number correctly.\nYou lost your money.")
            play_again()
        
def play_again():
    global rn1, rn2, rn3, rn4, rn5, rn6
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer == 'y': askbet()
    elif answer == 'n': quit()
    else: print("Invalid input. Please enter y, or n.")
        
print("\nWelcome to the Power Ball! Just enter a bet,\nthen type your numbers to see if you win!")
askbet()