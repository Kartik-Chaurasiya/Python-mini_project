import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate(password, letters, numbers, symbols, nl, nn, ns):
    cl, cn, cs = 0, 0, 0
    select_arr = [letters, numbers, symbols]
    while(cl + cs + cn != nl + nn + ns):
        selected = random.choice(select_arr)
        if (selected == letters) and (cl != nl):
            password += random.choice(letters)
            cl += 1
        elif (selected == numbers) and (cn != nn):
            password += random.choice(numbers)
            cn += 1
        elif (selected == symbols) and (cs != ns):
            password += random.choice(symbols)
            cs += 1
        else :
            continue
    print(cl, cn , cs)
    return password
     
print('Welcome to password generator.')
nl = int(input('Enter the number of leters character u want: '))
nn = int(input('Enter the number of number character u want: '))
ns = int(input('Enter the number of symbol character u want: '))
password = ''
print(generate(password, letters, numbers, symbols, nl, nn, ns))