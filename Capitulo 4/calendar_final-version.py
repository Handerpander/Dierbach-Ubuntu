# Calendar Year Program

# intitialization
terminate = False
days_in_month = (31, 28, 31, 30, 31, 31, 30, 31, 30, 31)

month_names = ('January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November',
              'December')

calendar_year = []
month_separator = format('', '8')
blank_week = format('', '21')
blank_col = format('', '3')

# prompt for years until quit 
while not terminate:

    #get year
    year = int(input('Enter year (yyyy) (-1 to quit): '))
    while (year < 1800 or year > 2099) and year != -1:
        year = int(input('INVALID - Enter year(1800-2099): '))
    
    if year == -1:
        terminate = True
    else:
        #determine if leap year
        if (year % 4 == 0) and (not (year % 100 == 0) or
            (year % 400 == 0)):
            leap_year = True
        else:
            leap_year = False

        # determine day of the week
        century_digits = year // 100
        year_digits = year % 100
        value = year_digits + (year_digits // 4)

        if century_digits == 18:
            value = value + 2
        elif century_digits == 20:
            value = value + 6
        
        # leap year check
        if not leap_year:
            value = value + 1
        
        # determine first day of month for Jan 1
        first_day_of_current_month = (value + 1) % 7

        # construct calendar fora all 12 months
        for month_num in range(12):
            month_name = month_names[month_num]

            # init for new month
            current_day = 1
            if first_day_of_current_month == 0:
                starting_col = 7
            else:
                starting_col = first_day_of_current_month

            current_col = 1
            calendar_week = ''
            calendar_month = []

            # add any needed leading space for first week of month
            while current_col < starting_col:
                calendar_week = calendar_week + blank_col
                current_col = current_col + 1
            
            # store month as separate weeks
            if (month_name == 'February') and leap_year:
                num_days_this_month = 29
            else:
                num_days_this_month = days_in_month[month_num]

            while current_day <= num_days_this_month:

                #store day of month in field of length 3
                calendar_week = calendar_week + \
                    format(str(current_day), '>3')
                
                #check if at last column of displayed week
                if current_col == 7:
                    calendar_month = calendar_month + [calendar_week]
                    calendar_week = ''
                    current_col = 1
                else:
                    current_col = current_col + 1
                
                # increment current day
                current_day = current_day + 1

            # fill out final row of month with needed blanks
            calendar_week = calendar_week + \
                blank_week[0:(7-current_col+1) * 3]
            calendar_month = calendar_month + [calendar_week]

            # reset values for next month
            first_day_of_current_month = current_col
            calendar_year = calendar_year + [calendar_month]
            calendar_month = []
        
    print(calendar_year)

    # reset for another year
    calendar_year = []

