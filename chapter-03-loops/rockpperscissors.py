import random,sys

def rockpaperscissors() :
    
    print('Rock,Paper,Scissors')

    wins=0
    losses=0
    ties=0
    rounds=5
    count=0
    
    while True:

        while True:
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            player_move=input('_')
            if player_move=='q':
                sys.exit()
            if player_move == 'r' or player_move == 'p' or player_move == 's':
                break
            print('Type one of r, p, s, or q.')

        if player_move == 'r':
            print('ROCK versus...')
        elif player_move == 'p':
            print('PAPER versus...')
        elif player_move == 's':
            print('SCISSORS versus...')
        move_number=random.randint(1,3)
        if move_number == 1:
            computer_move='r'
            print('Rock')
        elif move_number == 2:
            computer_move='p'
            print('Paper ')
        elif move_number == 3:
            computer_move='s'
            print('Scissors ')

        wins_check ={'r':'s', 'p':'r', 's':'p'}
        if player_move == computer_move:
            print('it is a tie')
            ties=ties+1
        elif wins_check[player_move] == computer_move:
            print('You win')
            wins = wins + 1
        else:
            print('You lose')
            losses = losses + 1
        count+=1
        if count==rounds:
            break
    #print('%s Wins, %s losses, %s Ties' % (wins, losses, ties), )
    print(f"{wins} wins, {losses} losses, {ties} ties")
    if wins>losses :
        #print('Congratulations you had', wins,'Wins' )
        print(f"Congratulations, you had {wins} wins ")
    elif wins==losses:
        #print('WOW, its a Stalemate, you had', wins,'Wins and', losses,'Losses')
        print(f'WOW, its a Stalemate, you had {wins} Wins and {losses} Losses')
    else: 
        #print('You came out short, you had', wins,"Wins")
        print(f'You came out short, you had {wins} Wins')
    print("GAME OVER")

counter=0

while counter<1:
    print("\nMENU\nPress 1 if you want to play\nPress 2 if you want to quit ")
    choice = int(input("_ "))
    counter+=1
    if choice == 1:
        rockpaperscissors()
    else:
        print("BYE")
        sys.exit()
while counter>=1:
    print("\nMENU\nPress 1 if you want to continue\nPress 2 if you want to quit ")
    choice = int(input("_ "))
    if choice == 1:
        rockpaperscissors()
    else:
        print("BYE")
        sys.exit()
    


