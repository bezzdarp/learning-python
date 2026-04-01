# This program is supposed to format the phone number

print('Welcome to FormatNum!')
print('To close the program enter \'!\'')


def format_num():
    user_number = input('\nEnter you phone number: ')
    if user_number == '!':
        print('The program was closed!')
        exit()
    elif not user_number.isdigit():
        print('The phone number must consist only of numbers!')
        format_num()
    elif len(user_number) != 11:
        print('The length of the number must be 11!')
        format_num()
    else:
        result = '+7 ' + user_number[1:4] +' ' + user_number[4:7] + '-' + user_number[7:9] + '-' + user_number[9:]
        print('Your result:', result)

while True:
    format_num()