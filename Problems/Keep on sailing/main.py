# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.destination = input()
    # the old sail method that you need to rewrite
    def sail(self):
        return "The {0} has sailed for {1}!".format(self.name, self.destination)


black_pearl = Ship("Black Pearl", 800)
print(black_pearl.sail())
