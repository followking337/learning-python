print('\nЗадача 1')
MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    if age < MIN_DRIVING_AGE:
        print(f'{name} еще рано садиться за руль')
    else:
        print(f'{name} может водить')


allowed_driving('tim', 17)
allowed_driving('bob', 18)
