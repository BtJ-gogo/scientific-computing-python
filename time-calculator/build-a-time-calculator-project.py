def add_month(str1, str2):
    return str(int(str1) + int(str2))


def subtract_month(str1, str2):
    return str(int(str1) - int(str2))


def add_minutes(str1, str2):
    return add_month(str1, str2)


def subtract_minutes(str1, str2):
    return subtract_month(str1, str2)


def add_time(start, duration, week_day=''):
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_time = []
    next_day = 0
    week_day_index = 0

    # convert to 24h
    start = start.split()
    start[0] = start[0].split(':')
    if start[1] == 'PM':
        start[0][0] = add_month(start[0][0], '12')

    # split duration
    duration = duration.split(':')

    # calculate start + duration
    new_time.append(add_month(start[0][0], duration[0]))
    new_time.append(add_minutes(start[0][1], duration[1]))
    if int(new_time[1]) >= 60:
        new_time[0] = add_month(new_time[0], '1')
        new_time[1] = subtract_minutes(new_time[1], '60')

    # calculate next day
    if int(new_time[0]) >= 24:
        next_day = int(new_time[0]) // 24
        new_time[0] = subtract_month(new_time[0], str(24 * next_day))

    # convert to ampm
    # am
    if int(new_time[0]) < 12:
        new_time.append('AM')
    # pm
    else:
        new_time[0] = subtract_month(new_time[0], 12)
        new_time.append('PM')

    # convert  0:00 to ampm time
    if new_time[0] == '0':
        new_time[0] = '12'

    # calculate day of week
    if week_day == '':
        if next_day == 0:
            new_time = f'{new_time[0]}:{new_time[1]:0>2} {new_time[2]}'
        elif next_day == 1:
            new_time = f'{new_time[0]}:{new_time[1]:0>2} {new_time[2]} (next day)'
        else:
            new_time = f'{new_time[0]}:{new_time[1]:0>2} {new_time[2]} ({next_day} days later)'
    else:
        week_day = week_day.lower()
        week_day = week_day.capitalize()
        week_day_index = week_days.index(week_day) + next_day

        while True:
            if week_day_index < 7:
                break
            else:
                week_day_index = week_day_index % 7

        if next_day == 0:
            new_time = f'{new_time[0]}:{new_time[1]:0>2} {new_time[2]}, {week_days[week_day_index]}'
        elif next_day == 1:
            new_time = f'{new_time[0]}:{new_time[1]:0>2} {new_time[2]}, {week_days[week_day_index]} (next day)'
        else:
            new_time = f'{new_time[0]}:{new_time[1]:0>2} {new_time[2]}, {week_days[week_day_index]} ({next_day} days later)'
    print(new_time)
    return new_time


add_time('8:16 PM', '466:02', 'tuesday')
