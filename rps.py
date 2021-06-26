import random

def play():

    user = input("What is your choice? \
        'r' for rock, \
            'p' for paper, \
                's' for scissors\n")

    computer = random.choice(['r', 'p','s'])

# r>s s>p p>r
 
    if user == computer:
        return 'It is a tie'
    
    if is_win(user, computer):
        return 'You win!'
    return 'You lost!'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') \
        or (player == 's' and opponent == 'p') \
             or (player == 'p' and opponent == 'r'):
             return True
