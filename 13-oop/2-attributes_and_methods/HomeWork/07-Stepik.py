print('\nЗадача 1')


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


jack = Dog("Jack", 4)
print(jack.description())  # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof"))  # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow"))  # распечатает 'Jack says Bow Wow'

print('\nЗадача 2. Stack. LIFO: Last In First Out')


class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if self.size() > 0:
            return self.values.pop()
        print("Empty Stack")

    def peek(self):
        if self.size() > 0:
            return self.values[-1]
        print("Empty Stack")

    def is_empty(self):
        return self.size() == 0  # return not self.values

    def size(self):
        return len(self.values)


s = Stack()
s.peek()             # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')        # кладем элемент 'cat' на вершину стека
s.push('dog')        # кладем элемент 'dog' на вершину стека
print(s.peek())      # распечатает 'dog'
s.push(True)         # кладем элемент True на вершину стека
print(s.size())      # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)          # кладем элемент 777 на вершину стека
print(s.pop())       # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())       # удаляем элемент True с вершины стека и печатаем его
print(s.size())      # распечатает 2
