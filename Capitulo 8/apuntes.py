# Opening for Reading

input_file = open('myfile.txt', 'r')

input_file = open('data/myfile.txt','r')

input_file = open('C:/mypythonfiles/data/myfile.txt','r')

input_file.close()

# Opening for Writing

output_file = open('mynewfile.txt', 'w')

output_file.close()

# Reading Text Files

input_file = \
    open('myfile.txt', 'r')
empty_str = ''

line = input_file.readline()

while line != empty_str:
    print(line)
    line = input_file.readline()

input_file.close()

# Writing Text Files

empty_str = ''
input_file = open('myfile.txt', 'r')
output_file = open('myfile_copy.txt', 'w')

line = input_file.readline()

while line != empty_str:
    output_file.write(line)
    line = input_file.readline()

output_file.close()

# String Traversal

space = ''
num_space = 0

line = input_file.readline()
for k in range(0, len(line)):
    if line[k] == space:
        num_space = num_space + 1

# for chr in line:
#     if chr == space:
#         num_space = num_space + 1


# String Methods

char = 'A'
if char not in ('A', 'B', 'C', 'D', 'E', 'F', 'G'):
    print('Invalid musical note found')

# char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or \
# char in 'abcdefghijklmnopqrstuvwxyz' or \
# char in '0123456789'

# if not credit_card.isdigit():
#     print('Invalid card number')

# if not part_num[0:3].isalpha():
#     print('Invalid part number')




