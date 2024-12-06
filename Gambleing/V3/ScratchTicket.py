import random
import tkinter as tk
from tkinter import messagebox

numbers = [' 1 ', ' 1 ', ' 1 ', ' 1 ', ' 1 ', ' 1 ',' 1 ', ' 1 ', ' 1 ', ' 1 ', ' 2 ',' 2 ',' 2 ',' 2 ',' 2 ',' 2 ', ' 3 ',' 3 ',' 3 ',' 3 ',' 3 ',' 4 ',' 4 ',' 4 ',' 4 ',' 4 ',' 4 ', ' 5 ', ' 5 ', ' 5 ', ' 5 ', ' 5 ', ' 5 ', ' 5 ', ' 5 ', ' 6 ',' 6 ',' 6 ',' 6 ',' 6 ',' 6 ',' 7 ',' 7 ',' 7 ',' 7 ',' 7 ',' 8 ',' 8 ',' 8 ',' 8 ',' 8 ', ' 10', ' 9 ',' 9 ', ' 10', ' 10', ' 10', ' 50', ' 50', '100']
betnum = 0
n1,n2,n3,n4,n5,n6 = 'X', 'X', 'X', 'X', 'X', 'X'

def bet():
    try:
        pass
    except ValueError:
        messagebox.showerror("Error", "Invalid bet. Please enter a positive integer.")

def edit(n):
    global betnum
    terminal.config(text=f'Congrats! You have won the {n}x prize!')
    terminal.update()
    betlabel.config(text=f'You won: ${betnum*n}')
    betlabel.update()
    
def checknum():
    global n1, n2, n3, n4, n5, n6
    print('Checking Number (step 3)')
    if n1 != 'X' and n2 != 'X' and n3 != 'X' and n4 != 'X' and n5 != 'X' and n6 != 'X':
        print('Number Detected (step 4)')
        if (n1 == n2 and n2 == n3) or (n1 == n2 and n2 == n4) or (n1 == n2 and n2 == n5) or (n1 == n2 and n2 == n6) or (n1 == n3 and n3 == n4) or (n1 == n3 and n3 == n5) or (n1 == n3 and n3 == n6) or (n1 == n4 and n4 == n5) or (n1 == n4 and n4 == n6) or (n1 == n5 and n5 == n6):
            edit(n1)
            print('Numbers n1 detected (step 5)')
            play_again()
        elif (n2 == n3 and n3 == n4) or (n2 == n3 and n3 == n5) or (n2 == n3 and n3 == n6) or (n2 == n4 and n4 == n5) or (n2 == n4 and n4 == n6) or (n2 == n5 and n5 == n6):
            edit(n2)
            print('Numbers n2 detected (step 5)')
            play_again()
        elif (n3 == n4 and n4 == n5) or (n3 == n4 and n4 == n5) or (n3 == n4 and n4 == n6) or (n3 == n5 and n5 == n6):
            edit(n3)
            print('Numbers n3 detected (step 5)')
            play_again()
        elif (n4 == n5 and n5 == n6):
            edit(n4)
            print('Numbers n4 detected (step 5)')
            play_again()
        else:
            terminal.config(text="No match.")
            terminal.update()
            betlabel.config(text="Bet: $0")
            betlabel.update()
            print('No Match (step 5)')
            play_again()
    else:
        print('No numbers detected (step 4)')

def reset():
    pass

def play_again():
    again = messagebox.askyesno('Play Again?', 'Do you want to play again?')
    if again == True:
        bet = 0
        reset()
    else: window.destroy()
        
def scratch(num,button):
    global number, n1, n2, n3, n4, n5, n6
    num = random.choice(numbers)
    if n1 == num: n1 = num
    elif n2 == num: n2 = num
    elif n3 == num: n3 = num
    elif n4 == num: n4 = num
    elif n5 == num: n5 = num
    elif n6 == num: n6 = num
    print("Number Scratched (step 1)")
    button.config(text=f'\n       {num}       \n')
    button.config(state=tk.DISABLED)
    print("Button Changed (step 2)")
    checknum()

window = tk.Tk()

b1 = tk.Button(window, text='\n        X        \n', command=lambda: scratch(n1,b1), font=('Arial', 18))
b1.grid(row=0, column=0)

b2 = tk.Button(window, text='\n        X        \n', command=lambda: scratch(n2,b2), font=('Arial', 18))
b2.grid(row=0, column=1)

b3 = tk.Button(window, text='\n        X        \n', command=lambda: scratch(n3,b3), font=('Arial', 18))
b3.grid(row=0, column=2)

b4 = tk.Button(window, text='\n        X        \n', command=lambda: scratch(n4,b4), font=('Arial', 18))
b4.grid(row=1, column=0)

b5 = tk.Button(window, text='\n        X        \n', command=lambda: scratch(n5,b5), font=('Arial', 18))
b5.grid(row=1, column=1)

b6 = tk.Button(window, text='\n        X        \n', command=lambda: scratch(n6,b6), font=('Arial', 18))
b6.grid(row=1, column=2)

betlabel = tk.Label(window, text=f'Bet: ${betnum}', font=('Arial', 16))
betlabel.grid(row=3, column=0, columnspan=3)

terminal = tk.Label(window, text='Press a number to scratch', font=('Arial', 16))
terminal.grid(row=2, column=0, columnspan=3)

window.resizable(False, False)
window.title('Lottery Scratcher')
window.mainloop()