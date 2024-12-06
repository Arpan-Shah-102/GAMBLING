import random
import time
import tkinter as tk

icons = ['🍒','💎','🔔','🍉','⭐','🍇',' 7 ','🥇','🥈','🥉']
winnings = 0
moneyspent = 0
auto = False

def spin():
    global moneyspent
    moneyspent += 10
    mspentlabel.config(text=f"Money spent: ${moneyspent}")
    mspentlabel.update()
    spinbutton.config(state=tk.DISABLED)
    autospinbutton.config(state=tk.DISABLED)
    for i in range(10):
        rs1, rs2, rs3 = random.choice(icons), random.choice(icons), random.choice(icons)
        machinelabel.config(text=f"{rs1} {rs2} {rs3}")
        machinelabel.update()
        time.sleep(0.1)
    calculate_winnings(rs1, rs2, rs3)
        
def calculate_winnings(rs1, rs2, rs3):
    global winnings, moneyspent, auto
    if rs1 == rs2 == rs3:
        terminal.config(text="Congratulations! You won $150!")
        terminal.update()
        winnings += 150
    elif rs1 == rs2 or rs1 == rs3 or rs2 == rs3:
        terminal.config(text="Congratulations! You won $10!")
        terminal.update()
        winnings += 10
    else:
        terminal.config(text="Sorry, you didn't win anything.")
        terminal.update()
        
    if auto == False:
        spinbutton.config(state=tk.ACTIVE)
        autospinbutton.config(state=tk.ACTIVE)
    mwonlabel.config(text=f"Money won: ${winnings}")
    mwonlabel.update()

def autospin():
    def check_spin():
        global auto
        ent = entbox.get()
        try:
            ent = int(ent)
            top.destroy()
            auto = True
            for i in range(ent):
                spin()
                time.sleep(0.25)
            auto = False
            spinbutton.config(state=tk.ACTIVE)
            autospinbutton.config(state=tk.ACTIVE)
        except ValueError:
            top.destroy()
            terminal.config(text="That was not a valid number.")
            terminal.update()
    top = tk.Toplevel()
    top.title("Autospin")
    top.resizable(False, False)
    tk.Label(top, text="Enter the number of spins:", font=("Arial", 16)).pack()
    entbox = tk.Entry(top, font=("Arial", 16))
    entbox.pack()
    tk.Button(top, text="Submit", command=lambda: check_spin(), font=("Arial", 16)).pack()

window = tk.Tk()

machinelabel = tk.Label(window, text="  0  0  0  ",font=("Arial", 60))
machinelabel.grid(column=0,row=0,columnspan=2)

terminal = tk.Label(window, text='Welcome to Slots!',font=("Arial", 12)  )
terminal.grid(column=0,row=1,columnspan=2)

mspentlabel = tk.Label(window, text='Money Spent: $0',font=("Arial", 16)  )
mspentlabel.grid(column=0,row=2,columnspan=2)

mwonlabel = tk.Label(window, text='Money Won: $0',font=("Arial", 16)  )
mwonlabel.grid(column=0,row=3,columnspan=2)

spinbutton = tk.Button(window, text="Spin", command=spin,font=("Arial", 16))
spinbutton.grid(column=0, row=4,sticky=tk.E)
autospinbutton = tk.Button(window, text="Autospin", command=autospin,font=("Arial", 16))
autospinbutton.grid(column=1, row=4,sticky=tk.W)

window.resizable(False, False)
window.title("Slot Machine")
window.mainloop()