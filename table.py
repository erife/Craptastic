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

    def clear_bets(self):
        self.report_status['placed_bets'] = {}

    def pay_bets(self, winning_bets):
        win_amount = 0
        for bet in winning_bets:
            placed_bet = self.report_status['placed_bets'][bet]
            if bet == '6':
                win_amount += placed_bet * (7/6)
            else:
                win_amount += placed_bet
        return win_amount

    def validate_bet(self, bet, bet_amount):
        if isinstance(bet_amount, int):
            if bet_amount > 0 and bet_amount <= self.report_status['bank']:
                if bet == 'pass':
                    return True
                elif bet in ('4', '5', '9', '10') and bet_amount % 5 ==0:
                    return True
                elif bet in ('6', '8') and bet_amount % 6 ==0: 
                    return True
        return False
    
