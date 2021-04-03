print(''' _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|                                                                                                
  ,ad8888ba,             88                        88                                           
 d8"'    `"8b            88                        88              ,d                           
d8'                      88                        88              88                           
88            ,adPPYYba, 88  ,adPPYba, 88       88 88 ,adPPYYba, MM88MMM ,adPPYba,  8b,dPPYba,  
88            ""     `Y8 88 a8"     "" 88       88 88 ""     `Y8   88   a8"     "8a 88P'   "Y8  
Y8,           ,adPPPPP88 88 8b         88       88 88 ,adPPPPP88   88   8b       d8 88          
 Y8a.    .a8P 88,    ,88 88 "8a,   ,aa "8a,   ,a88 88 88,    ,88   88,  "8a,   ,a8" 88          
  `"Y8888Y"'  `"8bbdP"Y8 88  `"Ybbd8"'  `"YbbdP'Y8 88 `"8bbdP"Y8   "Y888 `"YbbdP"'  88          
                                                                                                ''')
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
}
def calculator():
    n1 = float(input('Enter First number: '))
    n2 = float(input('Enter second number: '))
    operation = input('''
    Enter '+' for Addition,
    Enter '-' for Subtraction,
    Enter '*' for Multiplication
    Enter '/' for Division
    Enter Your choice: 
    ''')
    calculate = operations[operation]
    answer = calculate(n1, n2)
    print(f"{n1} {operation} {n2} = {answer}")
    next_operation = True
    while next_operation:
        user_choice = input(f"press 'yes' to continue with the result {answer} or 'no' to start again: ")
        if user_choice == 'yes':
            n3 = float(input("Enter the new number for operation: "))
            operation = input('''
    Enter '+' for Addition,
    Enter '-' for Subtraction,
    Enter '*' for Multiplication
    Enter '/' for Division
    Enter Your choice: 
            ''')
            n4 = answer
            calculate = operations[operation]
            answer = calculate(n4, n3)
            print(f"{n4} {operation} {n3} = {answer}")
        else:
            next_operation = False
            calculator()
calculator()