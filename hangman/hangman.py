import random

def start_game(word, guessed):
    guess = input('Enter the guess : ')
    if (guess in word) and (guess not in guessed):
        for x in range(len(word)):
            if (guessed[x] == '-') and (guess == word[x]): 
                guessed[x] =  guess
        print(''.join(guessed))
        return 0
    else :
        print('Wrong Guess')
        return -1
        
    

def stop_game(lives):
    if lives <=0:
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
print('Number of lives = 10')
print('Number of words = {}'.format(len(predict)))
print(len(predict)*'-')
while (lives > 0) and ('-' in guessed) :
    lives += start_game(predict, guessed)
stop_game(lives)

