from functools import total_ordering
#import functools
@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1 == person2)  # Output: False
print(person1 != person2)  # Output: True
print(person1 < person2)  # Output: False
print(person1 <= person2)  # Output: False
print(person1 > person2)  # Output: True
print(person1 >= person2)  # Output: True
