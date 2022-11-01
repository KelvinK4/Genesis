import random

class Dice:
    def roll(self):
        die_1 = [1,2,3,4,5,6]
        print(f"({random.choice(die_1)}, {random.choice(die_1)})")


red = Dice()
red.roll()

