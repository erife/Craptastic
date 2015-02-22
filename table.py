import random

class Table:

    def __init__(self):
        self.point = None
    
    def set_point(self, point=None):
        if(point in [4, 5, 6, 8, 9, 10]):
            self.point = point
        return self.point

    def is_on(self):
        return self.point != None

    def roll_dice(self):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dice_roll = die1 + die2
        return dice_roll

    def shoot(self):
        dice_roll = self.roll_dice()
        if(not self.is_on()):
            point = self.set_point(dice_roll)
        else:
            point = self.point
        return point
