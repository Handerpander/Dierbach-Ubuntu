daily_temps = {'sun': 68.8, 'mon': 70.2, 'tue': 67.2, 'wed': 71.8,
               'thur': 73.2, 'fri': 75.6, 'sat':74.0}

daynames = {'sun': 'Sunday', 'mon': 'Monday', 'tue': 'Tuesday',
            'wed': 'Wedsneday', 'thur': 'Thursday', 'fri': 'Friday',
            'sat': 'Saturday'}

# if daily_temps['sun'] > daily_temps['sat']:
#     print('Sunday was the warmer weekend day')
# else:
#     if daily_temps['sun'] < daily_temps['sat']:
#         print('Saturday was the warmer weekend day')
#     else:
#         print('Saturday and Sunday were equally warm')

print('This program will display the average temperature for a given day')
day = input("Enter 'sun', 'mon', 'tue', 'wed', 'thur', 'fri', or 'sat': ")
print('The average temperature for', daynames[day], 'was',
      daily_temps[day], 'degrees')

