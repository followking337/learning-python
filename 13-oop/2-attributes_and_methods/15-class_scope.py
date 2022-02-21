"""
CLASS SCOPE

    · Класс образует свое пространство имен:
        import [module]
            [module].[variable]            --> пространство имен модуля
            [module].[class].[variable]    --> пространство имен класса через сам класс
            [module].[instance].[variable] --> пространство имен класса через экземпляр

    · Методу класса не доступно пространство имен класса (в случае отсутствия self
        ищет имена в глобальной области видимости). Поэтому:

    · Варианты доступа к атрибутам класса через метод класса (методу класса доступно пространство имен класса):
        1. self.[attribute]    --> обращение через self и в случае отсутствия атрибутов экземпляра.
        2. [class].[attribute] --> обращение через класс.
        3. self.[property]     --> обращение через свойство @property.
        4. cls.[attribute]     --> обращение через cls @classmethod.
        5. [class].[attribute] --> обращение через @staticmethod.
"""

python_dev = 1
go_dev = 1
react_dev = 1


class DepartmentIT:

    python_dev = 4
    go_dev = 3
    react_dev = 2

    # ищет имена в глобальной области видимости
    def info(self):
        print('info:')
        print(python_dev, go_dev, react_dev)

    # ищет имена в области видимости класса, в случае если данные атрибуты отсутствуют в экземпляре
    def info1(self):
        print('info1:')
        print(self.python_dev, self.go_dev, self.react_dev)

    # ищет имена в области видимости класса
    def info2(self):
        print('info2:')
        print(DepartmentIT.python_dev, DepartmentIT.go_dev, DepartmentIT.react_dev)

    @property
    def info3(self):
        print('info3:')
        return self.python_dev, self.go_dev, self.react_dev  # property should return or yield something

    @classmethod
    def info4(cls):  # эквивалент метода info2(self)
        print('info4:')
        print(cls.python_dev, cls.go_dev, cls.react_dev)  # DepartmentIT.python_dev

    @staticmethod
    def info5():  # эквивалент метода info2(self)
        print('info5:')
        print(DepartmentIT.python_dev, DepartmentIT.go_dev, DepartmentIT.react_dev)

    def make_backend(self):
        print('Python and GO')

    def make_frontend(self):
        print('React')

    def hiring_python_dev1(self):
        self.python_dev = self.python_dev + 1

    def hiring_python_dev2(self):
        DepartmentIT.python_dev = DepartmentIT.python_dev + 1


it1 = DepartmentIT()
it1.info()   # ищет имена в глобальной области видимости
print()
it1.info1()  # ищет имена в области видимости класса, в случае если данные атрибуты отсутствуют в экземпляре
it1.info2()  # ищет имена в области видимости класса
print(it1.info3)  # @property
it1.info4()  # @classmethod
it1.info5()  # @staticmethod

print('\nhiring_python_dev1:')
print(it1.python_dev)
it1.hiring_python_dev1()
print(it1.__dict__)  # был создан локальный атрибут
print(it1.python_dev)
print(DepartmentIT.python_dev)  # при этом атрибут класса не изменен

print('\nhiring_python_dev2:')
it2 = DepartmentIT()
print(it2.python_dev)
it2.hiring_python_dev2()
print(it2.__dict__)  # не было создано локального атрибута
print(it2.python_dev)
print(DepartmentIT.python_dev)
