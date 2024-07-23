import random

done = False
wins, losses, ties = 0, 0, 0

names = { 'R' : "Rock" , 'P' : "Paper" , 'S' : "Scissors"}
loses = {'R' : 'P', 'P' : 'S', 'S': 'R'}

while not done:
    choice = input('Please provide your next move (R, P, S) or  (Q to quit):').upper()
    cpu_choice = random.choice(['R','P','S'])
    
    if choice == cpu_choice:
        print( f"It's a tie You both chose {names[choice]}")
        ties += 1
    elif choice in ['R','P','S']:
        if cpu_choice == loses[choice]:
            print(f'CPU Wins! you chose {names[choice]}, cpu chose {names[cpu_choice] }.')
            losses +=1
        else:
            print(f'You Win! you chose {names[choice]}, cpu chose {names[cpu_choice]}.')
            wins += 1
    elif choice == 'Q':
        done = True
    else:
        print('Invalid')
        
    print ( f'Current Status: {wins} Wins, {losses} Losses, {ties} Ties')