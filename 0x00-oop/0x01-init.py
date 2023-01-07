#!/usr/bin/python3

class Person:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hello Humans, my name is {}.".format(self.name))


p = Person("Dave")
p.sayHi()
c = Person("Charity")
c.sayHi()
