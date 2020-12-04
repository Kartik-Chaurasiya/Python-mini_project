def check(one, two, three, four, five, six, seven, eight, nine):
    global status
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

def single_player(dine):
    print('Get ready')
    tic_tac(1, '---')
    while(status != 'win' or status != 'lose' or status != 'draw'):
        if dine == 'one':
            num = int(input('Enter your pos [1 - 9]'))
            tic_tac(num, 'X')
            dine = 'two'
        else:
            num = int(input('Enter your pos [1 - 9]'))
            tic_tac(num, '0')
            dine = 'one'
        

def multi_player():
    tic_tac()

print('For Single Player Press s')
print('For Double Player Press d')
mode = input('Please select mode ')
one = '---'
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
if(mode == 's'):
    single_player(dine)
else:
    multi_player()