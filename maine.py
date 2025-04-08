print('Welcome to dodo')
def oddeven():
    try:
        no1 = int(input('Enter a number and we\'ll see if it is odd or even\n'))
        if (no1 % 2) == 0 and int:
            print('Even')
        elif (no1 %2) != 0 and int:
            print('Odd')
    except ValueError:
        print('Input a number this time')
    
    no2 = input('Would you like to go again? \n')
    if no2 in ('Y', 'yes', 'YES', 'Yes', 'y'):
        oddeven()
    elif no2 in ('N', 'no', 'NO', 'No', 'n'):
        Kr = input('Kamen Rider?')
        if Kr in ('Y', 'yes', 'YES', 'Yes', 'y'):
         def loops():
            colors = ["Red", "Green", "Yellow", "Black", "Blue"]
            KRider = "Rider"
            for y in colors:
                print(f' {y} {KRider}')
                loops()
        elif Kr in ('N', 'no', 'NO', 'No', 'n'):
            print('Goodbye ?')
            exit()
        else:
            print('Wrong')
    else:
        print('Wrong')
        
oddeven()

def arrae():
    nummason = [[3, 8, 1],[5, 7, 2],[9, 4, 6]]
    largest = nummason[0][0]
    for w in nummason:
        for v in w:
            if v > largest:
                largest = v
                print("Largest value:", largest)

arrae()