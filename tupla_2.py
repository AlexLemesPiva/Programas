'''
script that allows register and save user's pet. For each pet it will be requested weight, age, name, and type that will be stored
in a tuple. To allow the possibility to have multiple pets, multiple lists will be created, in other words, a list of tuples.
Also it will show a ciclical menu to register and consult pet's info.
'''
import os

REGISTER = 1
CONSULT = 2
EXIT = 0
pets = ()

def show_menu():
    os.system('cls')
    print(f'''           My pets
    {REGISTER}) register a pet
    {CONSULT}) look for a pet
    {EXIT})    EXIT''')

def register_pet(pets):
    print('         Register pet')
    name = input('Name: ')
    age = int(input('Age: '))
    weight = float(input('Weight: '))
    race = input('Type: ')
    pets.append( (name, age, weight, race) )
    

def consult_pet(pets):
    os.system('cls')
    print('         My pets')
    if len(pets) == 0:
        print('No pets registered')
    else:
        for pet in pets:
            name, age, weight, race = pet
            print(f'Name: {name}')
            print(f'age: {age}')
            print(f'weight: {weight}')
            print(f'race: {race}')
            print('---'*20)
            
def main():
    pets = []
    continuar = True
    while continuar:
        show_menu()
        opc = int(input('Choose an option: '))
        if opc == REGISTER:
            register_pet(pets)
        elif opc == CONSULT:
            consult_pet(pets)
        elif opc == EXIT:
            continuar = False
        else:
            print('Invalid Option')
        input('Press enter to continue')
    input('See you!')

if __name__ == '__main__':
    main()