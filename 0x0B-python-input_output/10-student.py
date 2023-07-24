#!/usr/bin/python3

"""THis module defines 'Student' class
    that deifines a student
"""


class Student:
    """Student class with attributes 'first_name'
        'last_name' and 'age'
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
#@staticmethod
    def to_json(self, attrs=None):
        obj = Student(self.first_name, self.last_name, self.age)
        if attrs is None:
            return obj.__dict__
        else:
            for i in range(len(attrs)):
                if isinstance(attrs[i], Student):
#if attrs[i] == 'first_name' or attrs[i] == 'last_name' or attrs[i] == 'age':
                    return obj.__dict__
                return 0
