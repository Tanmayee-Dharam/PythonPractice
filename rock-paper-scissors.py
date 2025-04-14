import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for papers, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])                        #computer will randomly choose one of these choices

#some rules in order to determine who wins
    if user  == computer:
        return 'It\'s a tie'

    #In this game we know that r>s, s>p, p> r
    if is_win(user,computer):
        return 'You won!'

    return 'You Lost!'

def is_win(player,opponent):
    # return true if player wins
    #  #In this game we know that r>s, s>p, p> r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent =='p') or (player == 'p' and opponent =='r'):
        return True

print(play())