import shelve

monday_schedule = ['Math', 'English language', 'System programming', 'Python']
tuesday_schedule = ['English language', 'HTML','Python', 'Football']
wednesday_schedule = ['Math', 'Chemistry', 'Java']
thursday_schedule = ['Math', 'Russian language', 'Swimming', 'System programming']
friday_schedule = ['Math', 'English language', 'System programming', 'Python']
saturday_schedule = ['Running', 'Math', 'Phys']

with shelve.open('schedules', writeback=True) as schedules:
    # schedules['monday_schedule'] = monday_schedule
    # schedules['tuesday_schedule'] = tuesday_schedule
    # schedules['wednesday_schedule'] = wednesday_schedule
    # schedules['thursday_schedule'] = thursday_schedule
    # schedules['friday_schedule'] = friday_schedule
    # schedules['saturday_schedule'] = saturday_schedule

    # schedules['thursday_schedule'].append('Running')

    # temp_list = schedules['thursday_schedule']
    # temp_list.append('Running')
    # schedules['thursday_schedule'] = temp_list

    schedules['saturday_schedule'].append('English language')

    for key in schedules:
        print(key, schedules[key])
