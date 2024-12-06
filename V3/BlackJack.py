from random import choice
import tkinter as tk
from tkinter import messagebox

characters = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']
dealer = [21,20,19,18,17,16]
bet = 0
playercards = 0
dealercards = choice(dealer)
cardlist = []
thing = False

def play_again():
    global thing
    thing = True
    def reset():
        global bet, playercards, dealercards, cardlist
        bet = 0
        playercards = 0
        dealercards = choice(dealer)
        cardlist = []
        clabel.config(text=f'Cards: []\nTotal: 0')
        terminal.config(text='Got card: 0')
        blabel.config(text=f'Bet: $0')
        window.update()
        get_bet()
    
    def destroy_all(): window.destroy()
    
    msg = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if msg == True: reset()
    else: destroy_all()

def hit():
    global playercards, thing
    card = choice(characters)
    cardlist.append(card)
    
    def change_ace(value):
        global playercards, dealercards, bet
        playercards += value
        top.destroy()
        clabel.config(text=f'Cards: {cardlist}\nTotal: {playercards}')
        hitbutton.config(state=tk.ACTIVE)
        staybutton.config(state=tk.ACTIVE)
        if playercards > 21:
            terminal.config(text=f'You busted! Dealer wins.\nYou: {playercards}, Dealer: {dealercards}\nYou: $0, Dealer: ${round(bet*2)}')
            terminal.update()
            play_again()
        
    if card == 'J' or card == 'K' or card == 'Q': playercards += 10
    elif card == 'A':
        hitbutton.config(state=tk.DISABLED)
        staybutton.config(state=tk.DISABLED)
        top = tk.Toplevel()
        top.title("Ace value")
        top.resizable(False, False)
        tk.Label(top, text="Choose your ace value:", font=("Arial", 24)).pack()
        tk.Button(top, text="1", command=lambda: change_ace(1), font=("Arial", 16)).pack()
        tk.Button(top, text="11", command=lambda: change_ace(11), font=("Arial", 16)).pack()
    else: playercards += card
    clabel.config(text=f'Cards: {cardlist}\nTotal: {playercards}')
    clabel.update()
    
    if playercards > 21:
        terminal.config(text=f'You busted! Dealer wins.\nYou: {playercards}, Dealer: {dealercards}\nYou: $0, Dealer: ${round(bet*2)}')
        terminal.update()
        play_again()

def stay():
    global dealercards, playercards, bet
    if playercards > 21:
        terminal.config(text=f'You busted! Dealer wins.\nYou: {playercards}, Dealer: {dealercards}\nYou: $0, Dealer: ${round(bet*2)}')
        terminal.update()
        play_again()
        
    elif dealercards == playercards:
        terminal.config(text=f'It\'s a draw!\nYou: {playercards}, Dealer: {dealercards}\nYou: ${bet}, Dealer: ${bet}')
        terminal.update()
        play_again()
        
    elif playercards == 21:
        terminal.config(text=f'You win!\nYou: {playercards}, Dealer: {dealercards}\nYou: ${round(bet*2)}, Dealer: $0')
        terminal.update()
        play_again()
    
    elif playercards > dealercards:
        terminal.config(text=f'You win!\nYou: {playercards}, Dealer: {dealercards}\nYou: ${round(bet*2)}, Dealer: $0')
        terminal.update()
        play_again()
        
    elif dealercards > playercards:
        terminal.config(text=f'Dealer wins.\nYou: {playercards}, Dealer: {dealercards}\nYou: $0, Dealer: ${round(bet*2)}')
        terminal.update()
        play_again()

def get_bet():
    def checkbet():
        global bet, thing
        bets = bet_entry.get()
        try:
            bets = int(bets)
            if bets < 0: messagebox.showerror("Error", "Invalid bet. Please enter a positive integer.")
            else:
                bet = int(bets)
                top.destroy()
                if thing == True:
                    staybutton.config(state=tk.ACTIVE)
                    hitbutton.config(state=tk.ACTIVE)
                    blabel.config(text=f'Bet: ${bet}')
                    blabel.update()
        except ValueError:
            messagebox.showerror("Error", "Invalid bet. Please enter a positive integer.")
    if thing == True:
        staybutton.config(state=tk.DISABLED)
        hitbutton.config(state=tk.DISABLED)
    top = tk.Tk()
    top.title("Enter bet")
    tk.Label(top, text="Enter your bet:", font=("Arial", 16)).pack()
    bet_entry = tk.Entry(top, font=("Arial", 16))
    bet_entry.pack()
    submit_button = tk.Button(top, text="Submit", command=checkbet, font=("Arial", 16)).pack()
    top.mainloop()

get_bet()
window = tk.Tk()

clabel = tk.Label(window, text=f'Cards: {cardlist}\nTotal: {playercards}', font=("Arial", 24))
clabel.grid(row=0, column=0, columnspan=3)

blabel = tk.Label(window, text=f'Bet: ${bet}', font=("Arial", 16))
blabel.grid(row=1, column=0, columnspan=3)

terminal = tk.Label(window, text='Got card: 0', font=('Arial', 12))
terminal.grid(row=2, column=0, columnspan=3)

hitbutton = tk.Button(window, text='Hit', command=hit, font=("Arial", 16))
hitbutton.grid(row=3, column=0,sticky=tk.E)

staybutton = tk.Button(window, text='Stay', command=lambda: stay(), font=("Arial", 16))
staybutton.grid(row=3, column=1)

window.resizable(False, False)
window.title("Blackjack")
window.mainloop()