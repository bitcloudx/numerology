def dateChecker():
    days = 1
    months = 1
    year1 = 19
    year2 = 0
    i = 0
    list_of_dates = []
    while i < 50000:
        if year2 <= 9:
         year2_format = '0'+str(year2)
        else:
            year2_format = str(year2)
        print('days ' + str(days))
        print('month ' + str(months))
        print('years ' + str(year1) + year2_format)
        print('\n')
        leap_years = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]
        sum_of_dates = days + months + year1 + year2
        dates = (str(months)+'/'+str(days)+'/'+str(year1)+year2_format)
        if sum_of_dates != 68:
            if days >= 31 and months in [1, 3, 5, 7, 8, 10, 12] or days >= 30 and months in [4, 6, 9, 11] or days >= 28 and months == 2 and year2 not in leap_years or days >= 29 and months == 2 and year2 in leap_years:
                print('month changer here')
                days = 1
                if months < 12:
                    months += 1
            else:
                print('another day')
                days += 1
            if months >= 12:
                months = 1
                print('year change here')
                if year2 < 99:
                    year2 += 1
            elif year2 >= 99:
                print('decade changer here')
                year2 = 0
                year1 += 1
        else:
            print('added')
            list_of_dates.append((dates))
            days+=1
        i+=1
    print('list of dates:')
    print(list_of_dates)

        
dateChecker()
