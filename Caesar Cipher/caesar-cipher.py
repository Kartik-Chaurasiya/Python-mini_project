#we can also do this using ord() function.
print('''       

  ,ad8888ba,                                                                      88             88                                 
 d8"'    `"8b                                                                     ""             88                                 
d8'                                                                                              88                                 
88            ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88            ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
Y8,           ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88            8b         88 88       d8 88       88 8PP""""""" 88          
 Y8a.    .a8P 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88            "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
  `"Y8888Y"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88             `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                     88                                             
                                                                                     88                                             

''')
def encode(message, shift, letters):
    encoded_message = ''
    for x in message:
        pos = letters.index(x)
        pos = (pos + shift)%25
        #%25 if the sum is greater than 25 eg. if pos = 25(for 'z') then for any shift the value will be greator than 25 for which there is no element in the letters list. This will also help us in maintaining tha loop eg. after 'z' comes 'a' and so on.
        encoded_message += letters[pos]
    print(f"Encoded Text: {encoded_message}")

def decode(message, shift, letters):
    decoded_message = ''
    for x in message:
        pos = letters.index(x)
        pos = abs(pos - shift)%25 
        #this is subtraction so using abs is good idea for getting the positive result.
        decoded_message += letters[pos]
    print(f"Decoded Text: {decoded_message}")

def caesar(user_operation, message, shilft, letters):
    new_message = ''
    for x in message:
        pos = letters.index(x)
        if user_operation == 'encode':
            pos = (pos + shift)%25 
        else:
            pos = abs(pos - shift)%25 
        new_message += letters[pos]
    print(f"{user_operation}d Text: {new_message}")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
    user_operation = input("Enter 'encode' for Encoding and 'decode' for decoding: ")
    message = input("Enter your message: ").lower()
    shift = int(input("Enter the amount of shift: "))
    # if user_operation == 'encode':
    #     encode(message, shift, letters)
    # else:
    #     decode(message, shift, letters)
    caesar(user_operation, message, shift, letters)
    #combining both the function(encode() and decode())
    result = input("Enter 'yes' to run Again or 'no' to Exit: ")
    if result == 'no':
        print('Thank You')
        should_continue = False

