import math

num = int(input('Enter number to compute factorial of: '))
valid_input = False

while not valid_input:
    try:
        result = math.factorial(num)
        print(result)
        valid_input = True
    except ValueError:
        print('Cannot compute the factorial of negative numbers')
        num = int(input('Please re-enter: '))

valid = False

while not valid:
    try:
        month = int(input('Enter current month (1-12): '))

        while month < 1 or month > 12:
            print('Invalid Input - Must be in the range 1-12')
            month = int(input('Enter current month (1-12): '))
        valid = True
    except ValueError:
        print('Invalid Month Value')

def getMonth():
    month = int(input('Enter current month (1-12): '))

    if month < 1 or month > 12:
        raise ValueError('Invalid MOnth Value')
    
    return month

valid = False

while not valid:
    try:
        month = getMonth
        valid = True
    except ValueError:
        print('Invalid Month Entry\n')
    # except ValueError as err_mesg:
        #print(err_mesg, '\n')


file_name = input('Enter file name: ')
empty_str = ''

input_file_opened = False

while not input_file_opened:
    try:
        input_file = open(file_name, 'r')
        input_file_opened = True

        line = input_file.readline()

        while line != empty_str:
            print(line.strip('\n'))
            line = input_file.readline()
    except IOError:
        print('File Open Error\n')
        file_name = input('Enter file name: ')