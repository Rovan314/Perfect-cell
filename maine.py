def game():
    G = input('1 for Rock, 2 for Paper and 3 for Scissors')
    if G in ('1'):
        print('Currently under construction, try again later, Goodbye?')
        exit()
    elif G in ('2'):
        print('Currently under construction, try again later, Goodbye?')
        exit()
    elif G in ('3'):
        print('Currently under construction, try again later, Goodbye?')
        exit()
    else:
        print('I don\'t understand, try that again')

while True:
    play = input('Welcome, wanna play? \n')
    if play in ("Yes", 'Y', "y", "yes", "YES"):
        game()
    elif play in ('No', "N", "n", "no", "YES"):
        print('Goodbye?')
        exit()
    else:
        print('I don\'t understand, try that again')