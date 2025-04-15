import random
def game():
    
    P = input('Rock, Paper or Scissor? Type in 1-3 respectively if you are lazy,').strip().upper()
    
    com = random.choice(['ROCK','PAPER','SCISSOR'])
    
    print(f'You chose {P} + and the PC chose {com}')

    if P not in ('ROCK','PAPER', 'SCISSOR', '1', '2', '3'):
        print('I don\'t understand, try that again')
        return game()
    elif P == com:
        print('It\'s a tie')
    elif P in ('ROCK', '1') and com in 'SCISSOR':
        print ('You won (＾＾)ｂ')
    elif P in ('PAPER','2') and com in 'ROCK':
        print('You won (＾＾)ｂ')
    elif P in ('SCISSOR','3') and com in 'PAPER':
        print('You won (＾＾)ｂ')
    else:
        print('The Computer won')

while True:
    play = input('Welcome, wanna play? \n')
    if play in ("Yes", 'Y', "y", "yes", "YES"):
        game()
    elif play in ('No', "N", "n", "no", "YES"):
        print('Goodbye?')
        exit()
    else:
        print('I don\'t understand, try that again')