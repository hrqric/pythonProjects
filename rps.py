import random

def play():
    user = input("Rock 'R', Paper 'P', Scissors 'S' ... ").lower()
    computer = random.choice(['r','p','s'])
    print(f'{user} vs {computer}')

    if computer == user:
        return 'tie'
    
    if user == 'r' and computer == 's':
        return 'User won!'
    elif user == 'p' and computer == 'r':
        return 'User won!'
    elif user == 's' and computer == 'p':
        return 'User won!'



    elif user == 'p' and computer == 's':
        return 'Computer won!'
    elif user == 'r' and computer == 'p':
        return 'Computer won!'
    elif user == 's' and computer == 'r':
        return 'Computer won!'
    
    

print(play())