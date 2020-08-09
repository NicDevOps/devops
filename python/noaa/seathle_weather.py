from datetime import date, datetime


file_csv = '/home/nick/projects/devops/python/noaa/noaa.csv'

D = {}

def date_creater(date_string):
    d = datetime.strptime(date_string, "%Y-%m-%d")
    return d.date()

def convert_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file.readline()
            step_2 = file.readline().strip()
            while step_2:
                step_3 = step_2.split(',')
                step_4 = [step_3[3][1:-1], step_3[5][1:-1], step_3[6][1:-1], step_3[4][1:-1]]
                try:
                    D[date_creater(step_4[0])] = [int(step_4[1]), int(step_4[2]), float(step_4[3])]
                except ValueError:
                    D[date_creater(step_4[0])] = [int(step_4[1]), int(step_4[2]), step_4[3]]
                step_2 = file.readline().strip()

    except FileNotFoundError:
        print("Unexpected exception")


def add_rainy(weather):
    for key, value in weather.items():
        try:
            if value[2] > 0.00:
                weather[key] = [value[0], value[1], value[2], True]
            if value[2] == 0.00:
                weather[key] = [value[0], value[1], value[2], False]
        except TypeError:
            continue


def consolidate(weather):

    yearly_weather = {}

    tmax_year = []
    tmin_year = []
    tmax_yt = 0
    tmin_yt = 0
    tmax_avg = 0
    tmin_avg = 0
    total_prcp = 0
    total_rainy_days = 0
    total_days = 0

    for key, value in D.items():
        try:
            if key:
                total_days += 1
            tmax_year.append(value[0])
            tmin_year.append(value[1])
            total_prcp += value[2]
        
        except TypeError:
            continue

        if value[3] == True:
            total_rainy_days += 1 

        if key.month == 12 and key.day == 31:
            for y in tmax_year:
                tmax_yt += y
            for y in tmin_year:
                tmin_yt += y
            tmax_avg += tmax_yt / len(tmax_year)
            tmin_avg += tmin_yt / len(tmin_year)

            yearly_weather[key.year] = [tmax_avg, tmin_avg, total_prcp, total_rainy_days, total_days]

            tmax_year = []
            tmin_year = []
            tmax_yt = 0
            tmin_yt = 0
            tmax_avg = 0
            tmin_avg = 0
            total_prcp = 0
            total_rainy_days = 0
            total_days = 0

    return yearly_weather


def year_info(year, yearly_weather):

    print('{:>10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('YEAR', 'AVG_TMAX', 'AVG_TMIN', 'TOTAL_PRCP', 'TOTAL_RAINY_DAYS', 'TOTAL_DAYS'))

    for key, value in yearly_weather.items():
        if key == year:
            return '{:>10d} | {:>10.2f} | {:>10.2f} | {:>9.2f}" | {:>16d} | {:>10d}'.format(key, value[0], value[1], value[2], value[3], value[4])

    return '{:^10d} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format(year, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')

def hottest(yearly_weather):
    tmax_avg = []
    for value in yearly_weather.values():
        tmax_avg.append(value[0])

    i = sorted(tmax_avg)
    tmax_avg = i[-1]

    for key, value in yearly_weather.items():
        if value[0] == tmax_avg:
            hottest_year = key, tmax_avg
     
    return hottest_year


def coldest(yearly_weather):
    tmin_avg = []
    for value in yearly_weather.values():
        tmin_avg.append(value[1])

    i = sorted(tmin_avg)
    tmin_avg = i[0]

    for key, value in yearly_weather.items():
        if value[1] == tmin_avg:
            coldest_year = key, tmin_avg
     
    return coldest_year

def rainiest_days(yearly_weather):
    TOTAL_RAINY_DAYS = []
    for value in yearly_weather.values():
        TOTAL_RAINY_DAYS.append(value[3])

    i = sorted(TOTAL_RAINY_DAYS)
    TOTAL_RAINY_DAYS = i[-1]

    for key, value in yearly_weather.items():
        if value[3] == TOTAL_RAINY_DAYS:
            rainiest_year = key, TOTAL_RAINY_DAYS
     
    return rainiest_year

def highest_prcp(yearly_weather):
    TOTAL_PRCP = []
    for value in yearly_weather.values():
        TOTAL_PRCP.append(value[2])

    i = sorted(TOTAL_PRCP)
    TOTAL_PRCP = i[-1]

    for key, value in yearly_weather.items():
        if value[2] == TOTAL_PRCP:
            rainiest_year = key, TOTAL_PRCP
     
    return rainiest_year
    
convert_file(file_csv)

add_rainy(D)


print()
print(D)


print(consolidate(D))
print()
print(year_info(2010, consolidate(D)))
print()
print(hottest(consolidate(D)))
print()
print(coldest(consolidate(D)))
print()
print(rainiest_days(consolidate(D)))
print()
print(highest_prcp(consolidate(D)))
print()