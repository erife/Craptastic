import random

class Table:

    def __init__(self):
        self.point = None
        self.is_on = False
        self.all_bets = {}
        self.open_bets = ["pass_line"]
        self.payouts = {'pass_line': 2, 'non_point': 1.5}
        self.bank = 100

    def status(self):
        status = {}
        status['is_on']  = self.is_on
        status['point'] = self.point
        status['placed_bets'] = self.all_bets
        status['open_bets'] = self.open_bets
        status['bank'] = self.bank
        return status
       
    def set_point(self, point=None):
        self.point = point
        self.set_is_on()
        return self.point

    def set_is_on(self):
        self.is_on= self.point != None
        return self.is_on

    def roll_dice(self):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dice_roll = die1 + die2
        return dice_roll

    def shoot(self):
        self.eval_roll(self.roll_dice())

    def eval_roll(self, dice_roll):
        if(not self.is_on):
            if(dice_roll in [4, 5, 6, 8, 9, 10]):
                point = self.set_point(dice_roll)
                self.open_point_bets()
            else:
                point = None
                if(dice_roll in [2,3,12]):
                    self.is_craps()
                else:
                    self.pay_pass()
        elif(dice_roll in [7,11] or self.point == dice_roll):
            self.point = None
            point = self.set_point()
        else:
            point = self.point
        return point
                
    def is_craps(self):
        self.clear_bets()
        return

    def reset_open_bets(self):
        self.open_bets = ["pass_line"]

    def open_point_bets(self):
        self.open_bets.append("non_point")

    def place_bet(self, bet):
        self.all_bets = dict(list(self.all_bets.items()) + list(bet.items()))
        self.change_bank(self.total_bet_values(bet), "minus")
        self.update_open_bets(bet)

    def update_open_bets(self, bet):
        for key, value in bet.items():
            self.open_bets.remove(key)

    def clear_bets(self):
        self.all_bets = {}
        self.reset_open_bets()

    def total_bet_values(self, bet):
        total_value = 0
        for key, value in bet.items():
            total_value += value
        return value
    
    def change_bank(self, bet_value, sign):
        if sign == 'add':
            self.bank += bet_value
        elif sign == 'minus':
            self.bank -= bet_value
        else:
            raise AttributeError("Invalid Sign: %s" % sign)
        
    def list_all_bets(self):
        return self.all_bets

    def payout(self, dice_roll):
        payouts = 0
        winning_bets = self.filter_winning_bets(dice_roll)
        for key, value in winning_bets.items():
            payouts += self.payouts[key]*value
        return payouts

    def pay_pass(self):
        has_pass_line_bet = "pass_line" in self.all_bets.keys()
        win_amount = self.all_bets["pass_line"] if has_pass_line_bet else 0
        self.change_bank(win_amount, 'add')

    def filter_winning_bets(self, dice_roll):
        if(dice_roll == self.point):
            winner = 'pass_line'
        else:
            winner = []
        winning_bets = {}
        for key, value in self.all_bets.items():
            if(winner == key):
                winning_bets[key] = value
        return winning_bets
