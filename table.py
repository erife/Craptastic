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

