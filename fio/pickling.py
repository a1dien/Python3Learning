#pickle
import pickle

honda = (
    'civic',
    'grey',
    '2019',
    (
        (1, 'James Brown'),
        (2, 'Jane White'),
        (3, 'Jake Green')
    )
)


with open ('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)



models = ['civic', 'accord','pilot']
owners = ['James Brown', 'Jane White', 'Jake Green']

with open ('honda.pickle', 'wb') as honda_file:
     pickle.dump(honda, honda_file)
     pickle.dump(models, honda_file)
     pickle.dump(owners, honda_file)
     pickle.dump(44444444444, honda_file)


with open ('honda.pickle', 'rb') as honda_retrieved:
    honda_from_file = pickle.load(honda_retrieved)
    models = pickle.load(honda_retrieved)
    owners = pickle.load(honda_retrieved)
    number = pickle.load(honda_retrieved)

print(honda_from_file)
model, color, year, owner_list = honda_from_file
print(model)
print(color)
print(year)
for owner in owner_list:
    owner_number, owner_name = owner
    print(owner_number, owner_name)


print (models)
print (owners)
print (number)