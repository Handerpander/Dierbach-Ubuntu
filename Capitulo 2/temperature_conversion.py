# Temperature Convesion Program (Fahrenheit to Celsius)

# This program will convert a temperture entered in Fahrenheit
# to the equivalent degrees in Celsius

# program greeting
print('THis program will conver degrees to fahrenheit to degrees Celsius')

# get temperature in Fahrenheit
fahren = float(input('Enter degrees Fahrenheit: '))

# calc degrees Celsius
celsius = (fahren - 32) * 5 / 9

# output degrees Celsius
print(fahren, 'degrees Fahrenheit equals',
      format(celsius, '.1f'), 'degrees Celsius')