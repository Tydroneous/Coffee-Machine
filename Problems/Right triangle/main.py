class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2

        if pow(self.c, 2) == pow(self.a, 2) + pow(self.b, 2):
            # calculate the area here
            self.s = 1 / 2 * (self.a * self.b)
        else:
            self.s = "Not right"


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
my_obj = RightTriangle(input_c, input_a, input_b)

print(my_obj.s)
