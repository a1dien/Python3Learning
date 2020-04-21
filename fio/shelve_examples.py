import shelve

with shelve.open('shelve_test') as cars:
    cars['opel'] = 'Germany'
    cars['ope'] = 'Germany'
    cars['ford'] = 'USA'
    cars['mazda'] = 'Japan'
    cars['reno'] = 'France'

    print(cars['ford'])
    print(cars['reno'])

    print('Wrong record before deleting: ' + str(cars.get('ope')))
    del cars['ope']
    print('Wrong record before deleting: ' + str(cars.get('ope')))

    cars['kia'] = 'South Korea'

    for key in cars:
        print(key + ':' + cars[key])

#print (cars['mazda']) block closed, exception