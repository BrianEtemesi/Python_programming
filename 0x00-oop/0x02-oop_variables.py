#!/usr/bin/python3

class Robot:

    # class variable counting the number of robots
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))

        # when a bot is created
        # adds to the population
        Robot.population += 1

    def die(self):
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def sayHi(self):
        print("Hello Humans, My name is {}, how may I help you?".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} Robots.".format(Robot.population))


droid = Robot("R-35")
droid.sayHi()
Robot.how_many()

droid1 = Robot("T-9")
droid1.sayHi()
Robot.how_many()

print("\n Robots can do some work here.\n")

print("Robots have finished their work. Lets destroy them")

droid.die()
droid1.die()


Robot.how_many()
