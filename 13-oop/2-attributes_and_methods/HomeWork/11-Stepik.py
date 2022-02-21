print('\nЗадача 1.1')


class Money:

    def __init__(self, dollar, cent):
        self.total_cents = [dollar, cent]

    @property
    def dollars(self):
        return self.total_cents[0]

    @dollars.setter
    def dollars(self, dollar):
        if isinstance(dollar, int) and dollar >= 0:
            self.total_cents[0] = dollar
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents[1]

    @cents.setter
    def cents(self, cent):
        if isinstance(cent, int) and 0 <= cent < 100:
            self.total_cents[1] = cent
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

print('\nЗадача 1.2')


class Money:

    def __init__(self, dollar, cent):
        self.total_cents = dollar * 100 + cent

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollar):
        if isinstance(dollar, int) and dollar >= 0:
            self.total_cents = dollar * 100 + self.cents
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cent):
        if isinstance(cent, int) and 0 <= cent < 100:
            self.total_cents = self.dollars * 100 + cent
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
