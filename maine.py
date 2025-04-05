print('Welcome to dodo')
while True:
    try:
        no1 = int(input('Enter a number and we\'ll see if it is odd or even\n'))
        if (no1 % 2) == 0 and int:
            print('Even')
        elif (no1 %2 != 0) and int:
            print('Odd')
    except: ValueError
    print('Input a number')

    no2 = input('Would you like to go again? \n')
    if no2 == ('Y', 'yes', 'YES', 'Yes', 'y'):
        continue
    elif no2 == ('N', 'no', 'NO', 'No', 'n'):
        print('Goodbye')
        break
    else:
        print('Wrong')
        break
