import random
element_matrix = ['-' for x in range(1, 10)] #fill all places with blank for the start

def put(pos, element, element_matrix):
    element_matrix[int(pos)] = element
    return element_matrix

def show_game(element_matrix):
    print(" " + element_matrix[0] + " | " + element_matrix[1] + " | " + element_matrix[2] + " ")
    print("-----------")
    print(" " + element_matrix[3] + " | " + element_matrix[4] + " | " + element_matrix[5] + " ")
    print("-----------")
    print(" " + element_matrix[6] + " | " + element_matrix[7] + " | " + element_matrix[8] + " ")

def is_winner(element, element_matrix):
    if((element_matrix[0] == element and element_matrix[1] == element and element_matrix[2] == element) or
    (element_matrix[3] == element and element_matrix[4] == element and element_matrix[5] == element) or
    (element_matrix[6] == element and element_matrix[7] == element and element_matrix[8] == element) or
    (element_matrix[0] == element and element_matrix[3] == element and element_matrix[6] == element) or
    (element_matrix[1] == element and element_matrix[4] == element and element_matrix[7] == element) or
    (element_matrix[2] == element and element_matrix[5] == element and element_matrix[8] == element) or
    (element_matrix[0] == element and element_matrix[4] == element and element_matrix[8] == element) or
    (element_matrix[2] == element and element_matrix[4] == element and element_matrix[6] == element)):
        return True
    else:
        return False


def is_empty(pos, element_matrix):
    num = [0,1,2,3,4,5,6,7,8]
    if (pos != ''):
        if (element_matrix[int(pos)] == '-'):
            return True
        else:
             return False
    else:
        return False

def two_player(element_matrix):
    player_status = input('Press "s" to start the Game : ')
    elements = ['X', '0']
    element = random.choice(elements)
    while(player_status == 's'):
        if (element == 'X'):
            pos = input("Enter the position to place X [ 0-8 ] : ")
            if (bool(is_empty(pos, element_matrix)) == True):
                element_matrix = put(pos, element, element_matrix)
                show_game(element_matrix)
                if (bool(is_winner(element, element_matrix)) == True):
                    print("{} is the winner".format(element))
                    break       
                element = "0"
            else:
                print("The position has been taken please enter another position or enter a proper number ")
                continue
        else:
            pos = input("Enter the position to place 0 [ 0-8 ] : ")
            if (bool(is_empty(pos, element_matrix)) == True):
                element_matrix = put(pos, element, element_matrix)
                show_game(element_matrix)
                if (bool(is_winner(element, element_matrix)) == True):
                    print("{} is the winner".format(element))
                    break       
                element = "X"
            else:
                print("The position has been taken please enter another position or enter a proper number ")
                continue

print("X & 0")
show_game(element_matrix)
print("Enter the GameType :")
print("1. Two Player mode : t")
print("1. Random Computer mode : r")
game_type = input("Enter your choice : ")
if (game_type == 't'):
    two_player(element_matrix)