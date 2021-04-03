import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
hands = [rock, paper, scissor]
print("Welcome to the game of ROCK, PAPER, SCISSOR'S")
user = input('''
Press 'R' for ROCK
Press 'P' for PAPER
Press 'S' for SCISSOR
''')
if user == 'R':
  print('Your choice: {}'.format(rock))
elif user == 'P':
  print('Your choice: {}'.format(paper))
else:
  print('Your choice: {}'.format(scissor))
comp = random.choice(hands)
print("Computer: {}".format(comp))
if((user == 'R' and comp == rock) or (user == 'P' and comp == paper) or (user == 'S' and comp == scissor)):
  print('''
       _                    
      | |                   
    __| |_ __ __ ___      __
   / _` | '__/ _` \ \ /\ / /
  | (_| | | | (_| |\ V  V / 
   \__,_|_|  \__,_| \_/\_/  
                          
  ''')

elif((user == 'R' and comp == scissor) or (user == 'P' and comp == rock) or (user == 'S' and comp == paper)):
  print('''     __                      
           \ / /  \ |  |    |  | | |\ | 
            |  \__/ \__/    |/\| | | \|                       
    ''')
else:
  print('''     __                __   __   ___ 
           \ / /  \ |  |    |    /  \ /__` |__  
            |  \__/ \__/    |___ \__/ .__/ |___                       
  ''')

