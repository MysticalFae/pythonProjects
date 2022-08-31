import random

def play():
    # asking user what they want to play with
    user = input("Choose -- Rock (r), Paper (p), Sissors (s): ")
    comp = random.choice(['r', 'p', 's'])  # will choose one of them at random
    print("\n")
    if user == comp:
        print("You tied!")
    if win(user, comp): # if win = true
        print("You won!")

    else:
        print("You lost!")
    print("Opponent choose " + comp)

def win(player, opp):
    # will return true if player wins
    if (player == 'r' and opp == 's') or (player == 's' and opp == 'p') or (player == 'p' and opp == 'r'):
        return True

play()