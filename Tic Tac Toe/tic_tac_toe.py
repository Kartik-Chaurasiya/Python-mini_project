def check(one, two, three, four, five, six, seven, eight, nine):
    global status
    if((one == 'X') and (two == 'X') and (three == 'X')): #all conditions for winning 
        status = 'Xwin'
    elif((one == '0') and (two == '0') and (three == '0')):
        status = '0win'
    elif((four == 'X') and (five == 'X') and (six == 'X')):
        status = 'Xwin'
    elif((four == '0') and (five == '0') and (six == '0')):
        status = '0win'
    elif((seven == 'X') and (eight == 'X') and (nine == 'X')):
        status = 'Xwin'
    elif((seven == '0') and (eight == '0') and (nine == '0')):
        status = '0win'
    elif((one == 'X') and (five == 'X') and (nine == 'X')):
        status = 'Xwin'
    elif((one == '0') and (five == '0') and (nine == '0')):
        status = '0win'
    elif((three == 'X') and (five == 'X') and (seven == 'X')):
        status = 'Xwin'
    elif((three == '0') and (five == '0') and (seven == '0')):
        status = '0win'
    elif((one != '---') and (two != '---') and (three != '---') and (four != '---') and (five != '---') and (six != '---') and (seven != '---') and (eight != '---') and (nine != '---')):
        status = 'draw'
    
def tic_tac(num, piece):   # num = for pos, piece = X / 0
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine  
              
    if num == 1:
        one = piece
    elif num == 2:
        two = piece
    elif num == 3:
        three = piece
    elif num == 4:
        four = piece
    elif num == 5:
        five = piece
    elif num == 6:
        six = piece
    elif num == 7:
        seven = piece
    elif num == 8:
        eight = piece
    else:
        nine = piece

    print('''                          
    {}|{}|{}
    {}|{}|{}
    {}|{}|{}
    '''.format(one, two, three, four, five, six, seven, eight, nine))
    check(one, two, three, four, five, six, seven, eight, nine)
    if status == 'Xwin':
        print('X wins')
    elif status == '0wins':
        print('0 wins')
    elif status == 'draw':
        print('Its A Draw')

def multi_player(dine):
    print('Get ready')
    tic_tac(1, '---')
    while(status=='ongoing'):
        if dine == 'one':
            num = int(input('Enter your pos [1 - 9]'))
            if num - 9 > 0 or num < 0:
                print('Enter valid number')
                continue
            tic_tac(num, 'X')
            dine = 'two'
        else:
            num = int(input('Enter your pos [1 - 9]'))
            tic_tac(num, '0')
            dine = 'one'
        

def comp_player():
    tic_tac()

print('For Double Player Press d')
print('For a game with Computer Player Press c')
mode = input('Please select mode ')
one = '---'                 #rather than using one , two we can use a array or list for simplisity
two = '---'
three = '---'
four = '---'
five = '---'
six = '---'
seven = '---'
eight = '---'
nine = '---'
status = 'ongoing'
dine = 'one'
if(mode == 'd'):
    multi_player(dine)
else:
    comp_player()