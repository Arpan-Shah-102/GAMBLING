import random

skills = [1,2,3,4,5,6,7,8,9,10]
names = ['Gojo','Jamarcus','Bob','Samuel','Derick','Barry','Jerry','Supercalifragilisticexpialidocious','Joe','Muhamid']
horses = []
rates = []
horsenum = 0
betnum = 0

class horse:
    global names, skills
    def speed(): return random.choice(skills)
    def stamina(): return random.choice(skills)
    def luck(): return random.choice(skills)
    def name():
        n = random.choice(names)
        names.remove(n)
        return n

def genhorses():
    for i in range(5):
        hname = horse.name()
        hspeed = horse.speed()
        hstamina = horse.stamina()
        hluck = horse.luck()
    
        statslist = [1,2,3]
        hidden = random.choice(statslist)
    
        horses.append(hname)
        if hname == 'Gojo': rates.append(0)
        else: rates.append((hspeed + hstamina + hluck)/3)
    
        if hidden == 1:
            rspeed = hspeed
            hspeed = "---"
        elif hidden == 2:
            rstamina = hstamina
            hstamina = "---"
        elif hidden == 3:
            rluck = hluck
            hluck = "---"
    
        if hname == 'Gojo':
            print(f'Horse {i+1}: Gojo')
            if hidden == 1:
                print('Speed:   ---')
                print('Stamina: 10')
                print('Luck:    10\n')
            elif hidden == 2:
                print('Speed:   10')
                print('Stamina: ---')
                print('Luck:    10\n')
            elif hidden == 3:
                print('Speed:   10')
                print('Stamina: 10')
                print('Luck:    ---\n')
        else:
            print(f'Horse {i+1}:',hname)
            print('Speed:  ',hspeed)
            print('Stamina:',hstamina)
            print('Luck:   ',hluck,'\n')

def bet():
    global horsenum, betnum
    try:
        horsenum = int(input('Enter the number of the horse you want to bet on: '))
        if horsenum < 1 or horsenum > 5:
            print('Please enter a number between 1 and 5.')
            return bet()
    except ValueError:
        print('Please enter a valid number.')
        return bet()
    
    try:
        betnum = int(input('Enter your bet: '))
        if betnum < 0:
            print('Please enter a positive number.')
            return bet()
    except ValueError:
        print('Please enter a valid number.')
        return bet()
    simrace()
    
def simrace():
    global horsenum, betnum
    horsenum = int(horsenum)
    rate = sorted(rates)

    if rates[horsenum-1] == rate[-1]:
        print('Congratulations! You won the race!')
        print('You won:',betnum*3)
        
    elif rates[horsenum-1] == rate[-2]:
        print('Congratulations! You won second in the race!')
        print('You made your money back!')
        
    elif rates[horsenum-1] == rate[-3]:
        print('You won third in the race!')
        print('You lost your money.')
        
    elif rates[horsenum-1] == rate[-4]:
        print('You were fourth in the race.')
        print('You lost your money.')
        
    elif rates[horsenum-1] == rate[-5]:
        print('You were last place in the race.')
        print('You lost your money.')
    playagain()

def displaystats():
    for i in range(5):
        print(f"Horse {i+1}: Name: {horses[i]}, Rating: {rates[i]}")
    print(f"Ordered Scores: {sorted(rates)[0]}",end='')
    for i in range (4):
        print(f', {sorted(rates)[i+1]}',end='')
    print('\n')

def reset():
    global names, horses,rates, horsenum, betnum
    print("")
    names = ['Gojo','Jamarcus','Bob','Samuel','Derick','Barry','Jerry','Supercalifragilisticexpialidocious','Joe','Muhamid']
    horses = []
    rates = []
    horsenum = 0
    betnum = 0

def playagain():
    global horses, rates, horsenum, betnum, names
    again = input("Would you like to play again? (y/n): ")
    if again == 'y':
        reset()
        genhorses()
        bet()
    elif again == 'ys':
        displaystats()
        reset()
        genhorses()
        bet()
    elif again == 'ns': displaystats()
    else: print("Thanks for playing!")

genhorses()
bet()