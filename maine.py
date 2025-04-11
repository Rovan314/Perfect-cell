def game():
    pass

while True:
    play = input('Welcome, wanna play? \n')
    if play in ("Yes", 'Y', "y", "yes", "YES"):
        game()
    elif play in ('No', "N", "n", "no", "YES"):
        print('Goodbye?')
        exit()
    else:
        print('I don\'t understand, try that again')