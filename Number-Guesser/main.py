import random
print('''
  _   _       _   _   __  __     ____  U _____ u   ____           ____     _   _ U _____ u ____    ____   U _____ u   ____     
 | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u     U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u\| ___"|/U |  _"\ u  
<|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/     \| |  _ / \| |\| | |  _|" <\___ \/<\___ \/  |  _|"   \| |_) |/  
U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <        | |_| |   | |_| | | |___  u___) | u___) |  | |___    |  _ <    
 |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\        \____|  <<\___/  |_____| |____/>>|____/>> |_____|   |_| \_\   
 ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_       _)(|_  (__) )(   <<   >>  )(  (__))(  (__)<<   >>   //   \\_  
 (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)     (__)__)     (__) (__) (__)(__)    (__)    (__) (__) (__)  (__) 
''')
print("Welcome to Number Guesser.")
def check(user_guess, number):
    if user_guess > number:
        print("Too high")
        return -1
    elif user_guess < number:
        print("Too low")
        return -1
    else:
        return 0
game_is_on = True
level = input("Enter 'hard' for hard level or 'easy' for easy level: ")
if level == 'easy':
    lives = 10
    print("You have got 10 chances....")
    number = random.randint(1, 101)
    while lives > 0 and game_is_on == True:
        user_guess = int(input("Enter your GUESS: "))
        if user_guess == number:
            game_is_on = False
            print("You guessed Right.")
        else:
            lives += check(user_guess, number)
            print(f"You have got {lives} chances....")
else:
    lives = 5
    print("You have got 5 chances....")
    number = random.randint(1, 101)
    while lives > 0 and game_is_on == True:
        user_guess = int(input("Enter your GUESS: "))
        if user_guess == number:
            game_is_on = False
            print("You guessed Right.")
        else:
            lives += check(user_guess, number)
            print(f"You have got {lives} chances....")