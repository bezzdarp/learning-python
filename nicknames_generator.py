# This program is supposed to create a cool nickname
# from user's first and last name

import random

print('Hello! This is NicknameGenerator.')

def main_menu():
    print('\n1 - Generate a nickname')
    print('2 - Close the program')
    user_input = input('Choose any action: ')
    if user_input == '1':
        generate_nickname_action()
    elif user_input == '2':
        print('\nThe program was closed!')
        exit()
    else:
        print('This action doesn\'t exist, try again!\n')
        main_menu()
    

def generate_nickname_action():
    user_name = input('\nEnter your first and last name: ')

    def generate_nick(user_name):
        nickname = ''
        for i in user_name.split():
            nickname += '_'
            nickname += i.lower()       
        return nickname.strip('_')

    if not user_name:
        print('You haven\'t entered anything, try again!')
        generate_nickname_action()
    else:
        nickname = generate_nick(user_name) + str(random.randint(1, 999))
        print('Ready! Your nickname is:', nickname)


while True:
    main_menu()





