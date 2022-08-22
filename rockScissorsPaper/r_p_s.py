import random


def rock_scissors_paper(func):
    def wrapper(*args, **kwargs):
        play_list = ["rock", "scissors", "paper"]
        play = random.choice(play_list)
        print(f"La Pc muestra {play}")
        func(*args, **kwargs)
        if play == "rock" and hand ==  "paper"\
        or play == "paper" and hand == "scissors"\
        or play == "scissors" and hand == "rock":
            print("You won")
        elif play == hand:
            print("Tie")
        else: 
            print("You Lost")
    return wrapper

hand = "paper"
@rock_scissors_paper
def my_turn(hand):
    print(f'Yo muestro {hand}')
    
    
if __name__ == '__main__':
    my_turn(hand)             