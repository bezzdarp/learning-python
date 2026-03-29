# This program is supposed to check user's password
# for reliability

print('Hello! This is PasswordValidator.')
print('To close the program enter "!"')

def validate_password():
    user_password = input('\nEnter your password: ')
    reliability = 0

    if user_password == '!':
        print('\nThe program was closed!')
        exit()
    elif not user_password.replace(' ', ''):
        print('You haven\'t entered anything, try again!')
        validate_password()
    else:
        if len(user_password) < 16:
            if len(user_password) < 8:
                reliability += 1
            else:
                reliability += 2
        else:
            reliability += 3
        
        for char in user_password:
            if char.isdigit():
                reliability += 1

        dict_description = {
            1: '(EXTREMELY UNSAFE)',
            2: '(UNSAFE)',
            3: '(NORMAL)',
            4: '(GOOD)',
            5: '(NICE)',
        }
        
        for key, value in dict_description.items():
            if reliability == key:
                description = value 
                break
            else:
                description = '(PERFECT)'
            
    print('Result:', reliability, description)
        

while True:
    validate_password()
