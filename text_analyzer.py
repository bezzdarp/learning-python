# This program is supposed to analyze any text
# for the presence of sentences, words, letters, etc.

print('Welcome to TextAnalyzer!')
print('To close the program enter \'!\'')


def analyze_text():
    user_text = input('\nEnter your text: ').strip().lower()

    if user_text == '!':
        exit()
    elif not user_text.replace(' ', ''):
        print('You haven\'t entered anything, try again!')
        analyze_text()
    else:
        sentences = ((user_text + ' ').count('. ') + 
                     (user_text + ' ').count('! ') +
                     (user_text + ' ').count('? '))
        words = user_text.count(' ') + 1
        letters = 0
        vowels = 0
        consonants = 0

        for char in user_text.replace(' ', ''):
            if char.isalpha():
                letters += 1
                if char in 'aeiou':
                    vowels += 1
                else:
                    consonants += 1

        print('\nSentences:', sentences)
        print('Words:', words)
        print('Letters', letters)
        print('Vowels:', vowels)
        print('Consonants:', consonants)
        

while True:
    analyze_text()