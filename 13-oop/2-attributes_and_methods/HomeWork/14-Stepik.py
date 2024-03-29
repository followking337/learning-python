class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f'Робот {name} был создан')

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @staticmethod
    def how_many():
        print(f'{Robot.population}, вот сколько нас еще осталось')


r2 = Robot("R2-D2")  # печатает "Робот R2-D2 был создан"
r2.say_hello()       # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many()     # печатает "1, вот сколько нас еще осталось"
r2.destroy()         # печатает "Робот R2-D2 был уничтожен"
