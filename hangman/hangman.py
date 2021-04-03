import random

def start_game(word, guessed):
    guess = input('Enter the guess : ')
    if (guess in word) and (guess not in guessed) and (len(guess) == 1):
        for x in range(len(word)):
            if (guessed[x] == '-') and (guess == word[x]): 
                guessed[x] =  guess
        print(''.join(guessed))
        return 0
    else :
        print('Wrong Guess')
        return -1

def hangman(lives):
    if lives == 10:
        print('''
          _______
         |/      
         |      
         |      
         |       
         |      
         |
        _|___
        ''')
    elif lives == 9:
        print('''
          _______
         |/      |
         |      
         |      
         |       
         |      
         |
        _|___
        ''')
    elif lives == 8:
        print('''
          _______
         |/      |
         |      (
         |      
         |       
         |      
         |
        _|___
        ''')
    elif lives == 7:
        print('''
          _______
         |/      |
         |      (_
         |      
         |       
         |      
         |
        _|___
        ''')
    elif lives == 6:
        print('''
          _______
         |/      |
         |      (_)
         |      
         |       
         |      
         |
        _|___
        ''')
    elif lives == 5:
        print('''
          _______
         |/      |
         |      (_)
         |       |
         |       
         |      
         |
        _|___
        ''')
    elif lives == 4:
        print('''
          _______
         |/      |
         |      (_)
         |      \|
         |       
         |      
         |
        _|___
        ''')
    elif lives == 3:
        print('''
          _______
         |/      |
         |      (_)
         |      \|/
         |       
         |      
         |
        _|___
        ''')
    elif lives == 2:
        print('''
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      
         |
        _|___
        ''')
    elif lives == 1:
        print('''
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      /
         |
        _|___
        ''')   
    

def stop_game(lives):
    if lives <=0:
        print('''
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      / \
         |
        _|___
        ''')    
        print('You Lose')
    else :
        print('You win')

words = [
    'python',
    'java',
    'c',
    'javascript',
    'php',
    'kotlin',
    'swift',
    'dart'
    ]

predict = random.choice(words)
guessed = len(predict)*['-']
lives = 10
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
print('Number of lives = 10')
print('Number of words = {}'.format(len(predict)))
print(len(predict)*'-')
while (lives > 0) and ('-' in guessed) :
    lives += start_game(predict, guessed)
    hangman(lives)
    print('Number of lives remaining : {}'.format(lives))
stop_game(lives)

