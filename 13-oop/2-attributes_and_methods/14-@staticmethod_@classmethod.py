"""
DECORATORS

    def method():
        {code}

        · обычная функция
        · не привязывается ни к классу ни к экземпляру
        · вызов возможен только от класса
        · применение, в случае если есть необходимость создать функцию внутри класса

    def method(self):
        {code}

        · обычный метод класса
        · привязывается к экземпляру через self
        · вызов возможен только от экземпляра

    @staticmethod
    def method():
        {code}

        · не привязывается ни к классу ни к экземпляру
        · вызов возможен от класса и от экземпляра
        · применение, в случае если есть необходимость создать функцию внутри класса

    @classmethod
    def method(cls):
        {code}

        · привязывается к классу через cls
        · вызов возможен от класса и от экземпляра
        · в случае с экземпляром, на место cls определяет класс экземпляра через магическую переменную __class__
        · применение, для обработки целого класса
"""


class Example:

    def function():
        print('function hello')

    def normal_method(self):
        print(f'normal method hello, {self}')

    @staticmethod
    def staticmethod():
        print('staticmethod hello')

    @classmethod
    def classmetod(cls):
        print(f'classmetod hello, {cls}')


a = Example()

print('\n\tfunction:')
Example.function()
# a.function()  # TypeError: hello() takes 0 positional arguments but 1 was given

print('\n\tnormal_method:')
# Example.normal_method()  # TypeError: instance_hello() missing 1 required positional argument: 'self'
a.normal_method()

print('\n\tstaticmethod:')
Example.staticmethod()
a.staticmethod()

print('\n\tclassmetod:')
Example.classmetod()
a.classmetod()
print(a.__class__)
