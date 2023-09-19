cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'subaru' :
        print(car.lower())
    else:
        print(car.title())

'audi' in cars