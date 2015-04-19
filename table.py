<<<<<<< HEAD
import random
import sqlite3
conn = sqlite3.connect('state.db')
c = conn.cursor()

class Table:

    DEFAULT_BANK = 100
    

    def __init__(self, id):
        self.storage()
        self.point = None
        self.is_on = False
        self.all_bets = {}
        self.open_bets = ["pass_line"]
        self.payouts = {'pass_line': 1, 'non_point': .75}
        self.bank = self.load_bank(id)

    def load_bank(self, id):
        row = c.execute('SELECT bank FROM status where id = ?', (id,)).fetchone()
        if row:
            return row[0]
        return self.DEFAULT_BANK
        
    def storage(self):
        c.execute("CREATE TABLE IF NOT EXISTS status (id varchar(32) primary key, bank int)")
        conn.commit()

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
            self.coming_out(dice_roll)
        else:
            is_craps = self.check_craps(dice_roll)
            is_point = self.check_point(dice_roll)
            if(is_point):
                self.pay_bet("pass_line")
                self.set_point()
            elif(is_craps):
                return
            else:
                self.pay_bet("non_point")
                return

    def coming_out(self, dice_roll):
        if(dice_roll in [4, 5, 6, 8, 9, 10]):
            self.set_point(dice_roll)
            self.open_point_bets()
        else:
            if(dice_roll in [2,3,12]):
                self.on_craps()
            else:
                self.pay_bet("pass_line")


    def check_craps(self, dice_roll):
        if(dice_roll in [7,11]):
            self.on_craps()
            return True
        return False

    def check_point(self, dice_roll):
        if(dice_roll == self.point):
            return True
        return False
    
    def on_craps(self):
        self.clear_bets()
        self.set_point()
        return

    def reset_open_bets(self):
        self.open_bets = ["pass_line"]

    def open_point_bets(self):
        self.open_bets.append("non_point")

    def place_bet(self, bet):
        bet_value = self.total_bet_values(bet)
        if(self.validate_bet(bet_value)):
            self.all_bets = dict(list(self.all_bets.items()) + list(bet.items()))
            self.change_bank(self.total_bet_values(bet), "minus")
            self.update_open_bets(bet)
            return True
        return False

    def validate_bet(self, bet):
        return bet <= self.bank
    
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
        c.execute("INSERT OR REPLACE INTO status(id, bank) VALUES(?, ?)", ('saved_table', self.bank))
        conn.commit()
        
    def list_all_bets(self):
        return self.all_bets


    def pay_bet(self, bet):
        has_bet = bet in self.all_bets.keys()
        bet_amount = self.all_bets[bet] if has_bet else 0
        multiplier = self.payouts[bet]
        win_amount = bet_amount*multiplier
        self.change_bank(win_amount, 'add')

=======
from copy import copy
class ArgumentException(Exception): pass
class Table():
    DEFAULT_STATUS = {
        'bank': 100,
        'available_bets': ['pass'],
        'placed_bets': {},
        'is_on': False
    }

    
    def __init__(self, status=DEFAULT_STATUS):
        self.report_status = copy(status)
>>>>>>> origin/master

        
    def status(self):
        return self.report_status

    def set_on(self):
        self.report_status['is_on'] = True

    def set_off(self):
        self.report_status['is_on'] = False

    def increment_bank(self, amount):
        self.report_status['bank'] += amount

    def decrement_bank(self, amount):
        self.report_status['bank'] -= amount

    def place_bet(self, bet, amount):
        if bet == 'pass':
            self.report_status['placed_bets'] = {bet: amount}
        elif bet in ['4', '5', '6', '8', '9', '10']:
            raise ArgumentException("That is not a valid bet when the table is off")
        else:
            raise ArgumentException("That is not a valid bet")

