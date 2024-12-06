import random
numbers = [1, 1, 1, 1, 1, 1,1, 1, 1, 1, 2,2,2,2,2,2, 3,3,3,3,3 ,4,4,4,4,4,4, 5, 5, 5, 5, 5, 5, 5, 5, 6,6,6,6,6,6, 7,7,7,7,7, 8,8,8,8,8, 10, 9,9, 10, 10, 10, 50, 50, 100]
chosennum = int
n1, n2, n3, n4, n5, n6 = 'X', 'X', 'X', 'X', 'X', 'X'
bet = 0

def getnum(n,cn, n1, n2, n3, n4, n5, n6, bet):
    try:
        bet = int(input('Enter how much you want to bet: '))
        scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
    except ValueError:
        print('Please enter a valid number.')
        getnum(n, cn, n1, n2, n3, n4, n5, n6, bet)

def quickprint(n1, n2, n3, n4, n5, n6):
    print(f'|-----------------------|')
    print(f'|   {n1}   |   {n2}   |   {n3}   |')
    print(f'|-----------------------|')
    print(f'|   {n4}   |   {n5}   |   {n6}   |')
    print(f'|-----------------------|')

def scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet):
    quickprint(n1, n2, n3, n4, n5, n6)        
    try:
        checknum(n1, n2, n3, n4, n5, n6, bet)
        cn = int(input('Enter a number to scratch: '))
        if cn > 6 or cn < 1:
            print('Please enter a number between 1 and 6.')
            scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
        else:
            if cn == 1:
                if n1 == 'X':
                    n1 = random.choice(n)
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
                else:
                    print("You already scratched this number.")
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
            elif cn == 2:
                if n2 == 'X':
                    n2 = random.choice(n)
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
                else:
                    print("You already scratched this number.")
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
            elif cn == 3:
                if n3 == 'X':
                    n3 = random.choice(n)
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
                else:
                    print("You already scratched this number.")
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
            elif cn == 4:
                if n4 == 'X':
                    n4 = random.choice(n)
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
                else:
                    print("You already scratched this number.")
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
            elif cn == 5:
                if n5 == 'X':
                    n5 = random.choice(n)
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
                else:
                    print("You already scratched this number.")
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
            elif cn == 6:
                if n6 == 'X':
                    n6 = random.choice(n)
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
                else:
                    print("You already scratched this number.")
                    scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)
    except ValueError:
        print('Please enter a valid number.')
        scratchnum(n, cn, n1, n2, n3, n4, n5, n6, bet)

def checknum(n1,n2,n3,n4,n5,n6, bet):
    if n1 != 'X' and n2 != 'X' and n3 != 'X' and n4 != 'X' and n5 != 'X' and n6 != 'X':
        if (n1 == n2 == n3) or (n1 == n2 == n4) or (n1 == n2 == n5) or (n1 == n2 == n6) or (n1 == n3 == n4) or (n1 == n3 == n5) or (n1 == n3 == n6) or (n1 == n4 == n5) or (n1 == n4 == n6) or (n1 == n5 == n6):
            print(f'Congratulations! You have won the {n1}x prize!')
            print(f'You won: {bet*n1}.')
            play_again()
        elif (n2 == n3 == n4) or (n2 == n3 == n5) or (n2 == n3 == n6) or (n2 == n4 == n5) or (n2 == n4 == n6) or (n2 == n5 == n6):
            print(f'Congratulations! You have won the {n2}x prize!')
            print(f'You won: {bet*n2}.')
            play_again()
        elif (n3 == n4 == n5) or (n3 == n4 == n5) or (n3 == n4 == n6) or (n3 == n5 == n6):
            print(f'Congratulations! You have won the {n3}x prize!')
            print(f'You won: {bet*n3}.')
            play_again()
        elif (n4 == n5 == n6):
            print(f'Congratulations! You have won the {n4}x prize!')
            print(f'You won: {bet*n4}.')
            play_again()
        else:
            print("You did not get any prize.")
            play_again()

def play_again():
    again = input('Do you want to play again? (y/n): ').lower()
    if again.lower() == 'y':
        numbers = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,2,2,2,2,2, 3,3,3,3,3 ,4,4,4,4,4,4, 5, 5, 5, 5, 5, 5, 5, 5, 6,6,6,6,6,6, 7,7,7,7,7, 8,8,8,8,8, 10, 9,9, 10, 10, 10, 50, 50, 100]
        chosennum = int
        n1, n2, n3, n4, n5, n6 = 'X', 'X', 'X', 'X', 'X', 'X'
        bet = 0
        getnum(numbers, chosennum, n1, n2, n3, n4, n5, n6, bet)
    else:
        print('Thank you for playing!')
        quit()

print('\nWelcome to the Scratch Number Game!')
getnum(numbers,chosennum, n1, n2, n3, n4, n5, n6, bet)