# Age in Seconds Program (Stage 1)
# This program will calculate a person's approximate age in seconds

import datetime

# Get month, day, year of birth
month_birth = int(input('Enter month born (1-12): '))
day_birth = int(input('Enter day born (1-31): '))
year_birth = int(input('Enter year born (4-digit): '))

# Get current month, day, year
current_month = datetime.date.today().month
current_day =datetime.date.today().day
current_year = datetime.date.today().year

# Test output
print('\nTHe date of birht read is: ', month_birth, day_birth,
      year_birth)

print('The current date read is: ', current_month, current_day,
      current_year)

# Age in Seconds Program (Stage 2)
# This program will calculate a person's approximate age in seconds

###import datetime

### Get month, day, year of birth
##month_birth = int(input('Enter month born (1-12): '))
##day_birth = int(input('Enter day born (1-31): '))
##year_birth = int(input('Enter year born (4-digit): '))

### Get current month, day, year
##current_month = datetime.date.today().month
##current_day =datetime.date.today().day
##current_year = datetime.date.today().year

# Determine number of seconds in a day, average month, and average year
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day

avg_numsecs_years = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_years // 12

## Test output
# print('numsecs_day ', numsecs_day)
# print('avg_numsecs_month = ', avg_numsecs_month)
# print('avg_numsecs_year', avg_numsecs_years)

# Calculate approximate age in seconds
numsecs_1900_dob = ((year_birth - 1900) * avg_numsecs_years) + \
                    (month_birth - (1 * avg_numsecs_month)) + \
                    (day_birth * numsecs_day)

numsecs_1900_today = ((current_year - 1900) * avg_numsecs_years) + \
                    ((current_month - 1) * avg_numsecs_month) + \
                    (current_day * numsecs_day)

age_in_secs = numsecs_1900_today - numsecs_1900_dob

# output results
print('\nYou are approximately', age_in_secs, 'seconds old')