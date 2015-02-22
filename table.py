import random

class Table:

    def __init__(self):
        self.point = None
        self.all_bets = {}
        self.payouts = {'pass_line': 2, 'non-point': 1.5}

        
    def set_point(self, point=None):
        if(point in [4, 5, 6, 8, 9, 10, None]):
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
        elif(self.is_craps(dice_roll) or self.point == dice_roll):
            point = self.set_point()
        else:
            point = self.point
        return point

    def is_craps(self, dice):
        return dice in [7, 11]

    def place_bet(self, bet):
        self.all_bets = dict(list(self.all_bets.items()) + list(bet.items()))

    def list_all_bets(self):
        return self.all_bets

    def payout(self, dice_roll):
        payouts = 0
        winning_bets = self.filter_winning_bets(dice_roll)
        for key, value in winning_bets.items():
            payouts += self.payouts[key]*value
        return payouts

    def filter_winning_bets(self, dice_roll):
        print(dice_roll)
        print(self.point)
        if(dice_roll == self.point):
            winner = 'pass_line'
        elif(not self.is_craps(dice_roll)):
            winner = 'point'
        else:
            winner = []
        winning_bets = {}
        for key, value in self.all_bets.items():
            if(winner == key):
                winning_bets[key] = value
        return winning_bets
