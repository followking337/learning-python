"""
1. Все является объектом
2. Каждый встроенный тип является классом и подклассом класса object
3. Любой класс наследуется от класса object
"""

print('\n\tisinstance():')
print(isinstance(34, object))  # является ли экземпляр классом object
print(isinstance([3, 4], object))  # является ли экземпляр классом object
print(isinstance(int, object))  # является ли встроенный тип int экземпляром класса object
print(isinstance(dict, object))  # является ли встроенный тип dict экземпляром класса object

print('\n\tissubclass():')
print(issubclass(int, object))  # является ли встроенный тип int подклассом класса object
print(issubclass(dict, object))  # является ли встроенный тип dict подклассом класса object


class Person(object):  # по умолчанию parent class Person наследуется от класса object
    pass  # данный класс наследует весь функционал (атрибуты и методы) от класса object


print('\n\tPerson():')
print(issubclass(Person, object))  # является ли тип Person подклассом класса object
a = Person()
print(isinstance(a, object))  # является ли экземпляр класса Person классом object

print('\n\tobject():')
print(issubclass(object, object))  # является ли тип object подклассом класса object
b = object()
print(isinstance(b, object))  # является ли экземпляр класса object классом object

print('\n\tПрименение:')
for variable in dir(object):  # list атрибутов и методов экземпляра класса object
    print(variable)
print(len(dir(object)))
print('-----------------------')

for variable in dir(Person):  # list атрибутов и методов экземпляра класса Person
    print(variable)
print(len(dir(Person)))
print('-----------------------')

print('\n\tНаследуемый функционал:')
print(a.__hash__())
print(a.__str__())
print(a == a)
print(b.__hash__())
print(b.__str__())


class Mylist(list):  # legacy: object --> list --> Mylist
    pass


print('\n\tMylist():')
t = Mylist()
print(t, type(t))
print(list(), type(list()))
t.append(78)
print(t, type(t))
print(issubclass(Mylist, list))
print(isinstance(t, Mylist))
print(isinstance(t, list))
print(isinstance(t, object))
