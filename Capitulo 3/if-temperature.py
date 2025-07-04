# Temperature Conversion Program (Celsius-Fahernheit / Fahrenheit-Celsisus)

# Display program welcome
print('THis program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')

# Get temperature to convert
which =input('Enter selection: ')
temp = int(input('Enter temperature to convert: '))

# Determine temperature conversion needed and display results
if which == 'F':
    converted_temp = (temp - 32) * 5/9
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
else:
    if which == 'C':
        converted_temp = (9/5 * temp) + 32
        print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')
    else:
        print('INVALID INPUT')