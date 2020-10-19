class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {}!".format(self.name)


my_person = Person(input())

print(my_person.greet())
