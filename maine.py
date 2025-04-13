import random
def game():
    
    P = input('Rock, Paper or Scissor? Type in 1-3 respectively if you are lazy,').strip().upper()
    
    com = random.choice(['ROCK','PAPER','SCISSOR'])
    
    if P in ('ROCK','1'):
        print('Currently under construction, try again later, Goodbye?')
        exit()
    elif P in ('PAPER','2'):
        print('Currently under construction, try again later, Goodbye?')
        exit()
    elif P in ('SCISSOR','3'):
        print('Currently under construction, try again later, Goodbye?')
        exit()
    else:
        print('I don\'t understand, try that again')
        return game()

while True:
    play = input('Welcome, wanna play? \n')
    if play in ("Yes", 'Y', "y", "yes", "YES"):
        game()
    elif play in ('No', "N", "n", "no", "YES"):
        print('Goodbye?')
        exit()
    else:
        print('I don\'t understand, try that again')