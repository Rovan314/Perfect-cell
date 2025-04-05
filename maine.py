print('Welcome to dodo')
def oddeven():
    try:
        no1 = int(input('Enter a number and we\'ll see if it is odd or even\n'))
        if (no1 % 2) == 0 and int:
            print('Even')
        elif (no1 %2) != 0 and int:
            print('Odd')
    except: ValueError
    print('Input a number this time')
    
    no2 = input('Would you like to go again? \n')
    if no2 in ('Y', 'yes', 'YES', 'Yes', 'y'):
        oddeven()
    elif no2 in ('N', 'no', 'NO', 'No', 'n'):
        print('Goodbye')
        exit()
    else:
        print('Wrong')
        
oddeven()