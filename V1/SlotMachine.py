import random
import time

icons = ['🍒','💎','🔔','🍉','⭐','🍇','7️⃣ ','🥇','🥈','🥉']
winnings = 0
moneyspent = 0

def spin(ms, w, a, l):
    ms += 10
    for i in range(10):
        rs1, rs2, rs3 = random.choice(icons), random.choice(icons), random.choice(icons)
        print("\n#--------------#")
        print(f"# {rs1} | {rs2} | {rs3} #")
        print("#--------------#")
        time.sleep(0.1)
    calculate_winnings(rs1, rs2, rs3, ms, w, a, l)
        
def calculate_winnings(rs1, rs2, rs3, ms, w, a, l):
    if rs1 == rs2 == rs3:
        print(f"\nCongratulations! You won $150!")
        w += 150
    elif rs1 == rs2 or rs1 == rs3 or rs2 == rs3:
        print(f"\nCongratulations! You won $10!")
        w += 10
    else: print("\nSorry, you didn't win anything.")
    print(f"Current winnings: ${w}, Money spent: ${ms}")
    if l == 1:
        for i in range(a-1):
            a -= 1
            spin(ms, w, a, l)
    play_again(rs1, rs2, rs3, ms, w)
        
def play_again(rs1, rs2, rs3, ms, w):    
    while True:
        choice = input("(S)pin or (Q)uit? ")
        try:
            spin(ms, w, int(choice), 1)
        except ValueError:
            if choice.lower() =='s': spin(ms, w, 1, 0)
            elif choice.lower() == 'q': quit()
            else:
                print("Invalid choice. Please try again.")
                play_again(rs1,rs2,rs3, ms, w)
        
print("Welcome to Slots!")
play_again(None, None, None, moneyspent, winnings)