#!/usr/bin/env python


class Animal(object):
    def scream(self):
        print("aieeeeeeeeeeee")

    def beep(self):
        print("beep (animal)")

class Robot():
    def beep(self):
        print("beep boop")

bases = Robot, Animal

class Dog(*bases):

    def bark(self):
        print("woof woof")

    def beep(self):
        for base in type(self).__bases__:
            if hasattr(base, 'beep'):
                f = getattr(base, 'beep')
                if callable(f):
                    getattr(base, 'beep')(self)
        print("Dog beeping")


d = Dog()  #  Dog d = new Dog()
d.bark()
type(d).bark(d)  # same!

print(d)

d.scream()

print(Dog.mro())
d.beep()
