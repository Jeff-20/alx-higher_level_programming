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

    def to_json(self):

        obj = Student(self.first_name, self.last_name, self.age)
        return obj.__dict__
