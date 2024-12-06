from random import choice
characters = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']
dealer = [21,20,20,19,19,18,18,17,17,16,16]

def give_cards(c, d, dc):
    try:
        bet = int(input('\nEnter your bet: '))
    except ValueError:
        give_cards(c, d, dc)    
    
    playercards = 0
    holdvar = None
    dealercards = choice(d)
    def got11(): return int(input('Enter your value for an Ace (1 or 11): '))
    for i in range(2):
        holdvar = choice(c)
        if holdvar == 'J' or holdvar == 'K' or holdvar == 'Q': playercards += 10
        elif holdvar == 'A':
            try:
                holdvar = got11()
                playercards += holdvar
            except ValueError: got11()
        else: playercards += holdvar
        print(f'Player card {i+1}: {holdvar}, Total: {playercards}')
    calculate_score(playercards, dealercards, dc, bet)

def calculate_score(p,d,dc,b):
    if p > 21:
        print(f'\nBust! Dealer wins.\nYou: {p}, Dealer: {d}\nYou: $0, Dealer: ${b*2}')
        play_again()
    elif p == 21: see_if_won(p,d,b)
        
    hors = input('Do you want to (h)it or (s)tay? ').lower()
    if hors == 'h':
        h = hit(dc, p)
        p += h
        print(f'\nDrawn card: {h}, Total: {p}')
    elif hors == 's': see_if_won(p,d,b)
    else:
        print('Invalid choice. Please try again.')
        calculate_score(p,d, dc, b)
    calculate_score(p,d,dc,b)

def hit(dc, p):
    def got11(): return int(input('Enter your value for an Ace (1 or 11): '))
    holdvar = choice(dc)
    if holdvar == 'J' or holdvar == 'K' or holdvar == 'Q': return 10
    elif holdvar == 'A':
        try:
            holdvar = got11()
            return holdvar
        except ValueError: got11()
    else: return holdvar

def see_if_won(p,d,b):
    if p > d:
        print(f'\nYou win!\nYou: {p}, Dealer: {d}\nYou: ${b*2}, Dealer: $0')
        play_again()
    elif p == d:
        print(f'\nIt\'s a draw!\nYou: {p}, Dealer: {d}\nYou: ${b}, Dealer: ${b}')
        play_again()
    elif p < d:
        print(f'\nDealer wins.\nYou: {p}, Dealer: {d}\nYou: $0, Dealer: ${b*2}')
        play_again()

def play_again():
    global characters, dealer
    choice = input('Do you want to play again? (y/n): ').lower()
    if choice == 'y': give_cards(characters, dealer, characters)
    elif choice == 'n': quit()
    else: play_again()

print('\nWelcome to simple blackjack!',end="")
give_cards(characters, dealer, characters)