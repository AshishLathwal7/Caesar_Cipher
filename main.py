from art import logo
from functions import shift

print(logo)

loop_continue = True

#if a message/code is not in small alphabets, it will not print desired output
print("Please enter the message in small alphabets only!")
while True:
    choice = input("Plese enter 'en' to encrypt or 'de' for decrypt. \n ")
    msg = input(f"Enter the message for {choice}crypt. \n")
    key = int(input(f"Enter the {choice}cryption key.(integer value) \n"))

    if choice == 'en':
        pass
    elif choice == 'de':
        key = -key
    else: 
        print("please enter the correct input for encrypt/decrypt")
        continue

    result = shift(msg= msg, key= key)

    print(f'Here is the {choice}crypted message: {result}')

    y = input("Type 'y' to run the program again or anykey to close the program.\n" )
    
    if y != 'y': loop_continue = False


