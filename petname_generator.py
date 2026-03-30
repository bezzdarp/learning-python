# This program is supposed to generate a cool name
# for your pet 

import random

print('Welcome to PetnameGenerator!')

pet_names = [
    "Max", "Charlie", "Cooper", "Jack", "Rocky",
    "Buddy", "Milo", "Bear", "Leo", "Tucker",
    "Luna", "Bella", "Lucy", "Daisy", "Molly",
    "Lola", "Stella", "Chloe", "Sophie", "Zoe",
    "Oliver", "Simba", "Oscar", "Jasper", "Finn",
    "Coco", "Ginger", "Pepper", "Shadow", "Smokey",
    "Nala", "Cleo", "Mochi", "Mochi", "Loki",
    "Zeus", "Oreo", "Misty", "Sadie", "Rosie",
    "Ruby", "Maggie", "Gracie", "Bailey", "Harley",
    "Toby", "Winston", "Duke", "Riley", "Sam"
]


def generate_petname():
    user_input = input('\nWanna generate a name for your pet?\nYes/No: ').lower()
    if user_input.startswith('ye'):
        petname = pet_names[random.randint(0, len(pet_names) - 1)]
        print('Ready! We got', petname)
    elif user_input.startswith('no'):
        print('\nWhy? OK, bye...')
        exit()
    else:
        print('\nYou\'re weird, bye!')
        exit()


while True:
    generate_petname()