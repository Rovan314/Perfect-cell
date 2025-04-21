import random
from enum import Enum
    
class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    
    @classmethod
    def from_input(cls, input_str):
        input_str = input_str.strip().upper()
        if input_str in ('1', 'ROCK'):
            return cls.ROCK
        elif input_str in ('2', 'PAPER'):
            return cls.PAPER
        elif input_str in ('3', 'SCISSOR'):
            return cls.SCISSOR
        else:
            return None

Pwin = 0
Cwin = 0

def game():
    global Pwin, Cwin
    P_input = input('Rock, Paper or Scissor? Type in 1-3 respectively if you are lazy: ').strip().lower()
    P = Move.from_input(P_input)

    if not P:
        print("I don't understand, try that again")
        return game()
    
    com = random.choice(list(Move))

    print(f'You chose {P.name} and the PC chose {com.name}\n')

    if P == com:
        print("It's a tie")
    elif P == Move.ROCK and com == Move.SCISSOR:
        print ('You won (＾＾)ｂ')
        Pwin += 1
    elif P == Move.PAPER and com == Move.ROCK:
        print('You won (＾＾)ｂ')
        Pwin += 1
    elif P == Move.SCISSOR and com == Move.PAPER:
        print('You won (＾＾)ｂ')
        Pwin += 1
    else:
        print('The Computer won')
        Cwin += 1
    
    print(f'\nYou won {Pwin} times and the Computer won {Cwin}\n')
    
    if Pwin > Cwin:
        print('Looks like you are in the lead\n')
    elif Pwin < Cwin:
        print('The Computer is in the lead')
    else:
        print('So far it looks like an even game')

    while True:
            final = input('Want to play again? \n')
            if final in ("Yes", 'Y', "y", "yes", "YES"):
                game()
            elif final in ('No', "N", "n", "no"):
                print('Goodbye?')
                exit()
            else:
                print('I don\'t understand, try that again')
                continue

def play():
    while True:
        play = input('Welcome, wanna play? \n')
        if play in ("Yes", 'Y', "y", "yes", "YES"):
            game()
        elif play in ('No', "N", "n", "no", "YES"):
            print('Goodbye?')
            exit()
        else:
            print('I don\'t understand, try that again')
            continue
play()