import shelve

university = shelve.open('university_file')
# university["schedules"] = {
#         'monday_schedule' : ['Math', 'English language', 'System programming', 'Python'],
#         'tuesday_schedule' : ['English language', 'HTML','Python', 'Football'],
#         'wednesday_schedule' : ['Math', 'Chemistry', 'Java'],
#         'thursday_schedule' : ['Math', 'Russian language', 'Swimming', 'System programming'],
#         'friday_schedule' : ['Math', 'English language', 'System programming', 'Python'],
#         'saturday_schedule' : ['Running', 'Math', 'Phys']
#     }
# university["tutors"] = {
#         "Math": ['Jack White', 'Jim Black'],
#         'Python':['Youra', 'Jane Smith']
#     }
#
print(university['schedules']['wednesday_schedule'])
print(university['tutors']['Math'])
#
university.close()


# university = {
#     "schedules": {
#         'monday_schedule' : ['Math', 'English language', 'System programming', 'Python'],
#         'tuesday_schedule' : ['English language', 'HTML','Python', 'Football'],
#         'wednesday_schedule' : ['Math', 'Chemistry', 'Java'],
#         'thursday_schedule' : ['Math', 'Russian language', 'Swimming', 'System programming'],
#         'friday_schedule' : ['Math', 'English language', 'System programming', 'Python'],
#         'saturday_schedule' : ['Running', 'Math', 'Phys']
#     },
#     "tutors": {
#         "Math": ['Jack White', 'Jim Black'],
#         'Python':['Youra', 'Jane Smith']
#     }
# }
# print(university['schedules']['wednesday_schedule'])
# print(university['tutors']['Math'])
#
