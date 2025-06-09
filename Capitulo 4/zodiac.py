# Chinese Zodiac Program

import datetime

#init
zodiac_animals = ('Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
                  'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig')

rat = 'Forthright, industriosu, sensitive, intellectual, sociable'
ox = 'Dependable, methodical, modest, born leader, patient'
tiger = ''
rabbit = ''
dragon = ''
snake = ''
horse = ''
goat = ''
monkey = ''
rooster = ''
dog = ''
pig = ''

characteristics = (rat, ox, tiger, rabbit, dragon, snake, horse, goat, monkey,
                   rooster, dog, pig)

terminate = False

# program greetign
print('This program will display your Chinese zodiac sign and associated')
print('personal characteristics. \n')

#get current year from module datetime
current_yr = datetime.date.today().year

while not terminate:

    #get year of birth
    birth_year = int(input('Enter yoyr year of birth (yyyy): '))

    while birth_year < 1900 or birth_year > current_yr:
        print('Invalid year. Please re-enter\n')
        birth_year = int(input('Enter your year of birth (yyyy): '))

        #output results
        cycle_num = (birth_year - 1900) % 12

        print('Your Chinese zodiac sign is the', zodiac_animals[cycle_num], '\n')
        print('Your personal cahracteristics ...')
        print(characteristics[cycle_num])

        #continue?
        response = input('\nWould you like to enter another year? (y/n): ')

        while response != 'y' and response != 'n':
            response = input("Please enter 'y' or 'n': ")

        if response == 'n':
            terminate = True