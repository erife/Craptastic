import unittest
from copy import copy
from table import Table
from table import ArgumentException

class TableTest(unittest.TestCase):
    INITIAL_STATUS = {
            'bank': 100,
            'is_on': False,
            'available_bets': ['pass'],
            'placed_bets': {}
        }

    ROLLS = {
        'snake_eyes':   [1, 1],
        'ace_deuce':    [1, 2],
        'easy_four':    [1, 3],
        'five':         [1, 4],
        'five_fever':   [2, 3],
        'six':          [1, 5],
        'hard_four':    [2, 2],
        'easy_six':     [2, 4],
        'hard_six':     [3, 3],
        'seven_out_1':  [1, 6],
        'seven_out_2':  [2, 5],
        'seven_out_3':  [3, 4],
        'easy_eight_1': [2, 6],
        'easy_eight_2': [3, 5],
        'hard_eight':   [4, 4],
        'easy_nine_1':  [3, 6],
        'easy_nine_2':  [4, 5],
        'easy_ten':     [4, 6],
        'hard_ten':     [5, 5],
        'yo_leven':     [5, 6],
        'boxcars':      [6, 6]
    }

    CRAPS_ROLLS = [
        'snake_eyes',
        'ace_deuce',
        'boxcars'
    ]

    def setUp(self):
        self.initial_status = copy(self.INITIAL_STATUS)


    def test_process_result_natural_coming_out(self):
        expected_result = {
            'winners': ['pass'],
            'is_on': False,
            'clear_pass_bets': False,
            'clear_number_bets': False
        }

        table = Table()

        rolls = ['seven_out_1', 'seven_out_2', 'seven_out_3', 'yo_leven']
        for roll in rolls:
            dice = self.ROLLS[roll]
            result = table.process_roll(dice)
            self.assertEqual(expected_result, result)

    def test_process_result_craps_coming_out(self):
        expected_result = {
            'winners': ['dont_pass'],
            'is_on': False,
            'clear_pass_bets': True,
            'clear_number_bets': False
        }

        table = Table()

        rolls = ['snake_eyes', 'ace_deuce', 'boxcars']
        for roll in rolls:
            result = table.process_roll(self.ROLLS[roll])
            self.assertEqual(expected_result, result)


    def test_is_craps_valid(self):
        self.initial_status['is_on'] = False
        table = Table(self.initial_status)
        for roll in self.CRAPS_ROLLS:
            result = table.is_craps(self.ROLLS[roll])
            self.assertEqual(True, result)

    def test_is_craps_invalid(self):
        self.initial_status['is_on'] = False
        table = Table(self.initial_status)
        table = Table(self.initial_status)
        for roll in self.ROLLS.keys() - self.CRAPS_ROLLS:
            result = table.is_craps(self.ROLLS[roll])
            self.assertEqual(False, result)

    def test_winners(self):
        self.initial_status['is_on'] = False
        table = Table(self.initial_status)
        result = table.get_winners(table.is_craps)
        expected_result = ['dont_pass']

        self.assertEqual(expected_result, result)


    def test_initial_status(self):
        table = Table()
        expected_result = self.initial_status

        result = table.status()
        self.assertEqual(expected_result, result)


    def test_altered_status(self):
        status = {
            'bank': 50,
            'is_on': True,
            'available_bets': ['4', '5', '6', '8', '9', '10'],
            'placed_bets': {'6': 1}
        }
        
        table = Table(status)
        expected_result = status
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
 
    def test_set_status_on(self):
        table = Table()
        
        expected_result = self.initial_status
        expected_result['is_on'] = True
        table.set_on()
        
        result = table.status()
        self.assertEqual(expected_result, result)
 

 
    def test_set_status_off(self):
        initial_status = self.initial_status
        initial_status['is_on'] = True
        table = Table(initial_status)
 
        expected_result = self.INITIAL_STATUS
        table.set_off()
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
    def test_increment_bank(self):
        table = Table()
        
        expected_result = self.initial_status
        expected_result['bank'] = 101
 
        table.increment_bank(1)
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
    def test_decrement_bank(self):
        table = Table()
        
        expected_result = self.initial_status
        expected_result['bank'] = 99
 
        table.decrement_bank(1)
        
        result = table.status()
        self.assertEqual(expected_result, result)


    def test_place_bet(self):
        table = Table()
        
        expected_result = self.initial_status
        expected_result['placed_bets'] = {'pass': 1}
 
        table.place_bet('pass', 1)
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
        table.place_bet('pass', 1)
        expected_result['placed_bets'] = {'pass': 2}
        
        for bet in ['-3', '1', '0', '13']:
            with self.assertRaisesRegex(ArgumentException, "That is not a valid bet"):
                table.place_bet(bet, 1)
                
        for bet in ['4', '5', '6', '8', '9', '10']:
            with self.assertRaisesRegex(ArgumentException, "That is not a valid bet when the table is off"):
                table.place_bet(bet, 1)
                
 
    def test_clear_bets(self):
        
        expected_result = self.INITIAL_STATUS
        
        self.initial_status['placed_bets'] = {'pass': 1}
        table = Table(self.initial_status)
 
        table.clear_bets()
        
        result = table.status()
        self.assertEqual(expected_result, result)

    def test_payout_bet(self):
        bet_amount = 1
        initial_status = copy(self.INITIAL_STATUS)
        initial_status['placed_bets'] = {'pass': bet_amount}
        table = Table(initial_status)
        
        
        winning_bets = ['pass']
        result = table.pay_bets(winning_bets)
        
        expected_result = bet_amount
        
        self.assertEqual(expected_result, result)


    def test_payout_bets(self):
        bet_amount = 6
        initial_status = copy(self.INITIAL_STATUS)
        initial_status['placed_bets'] = {'pass': bet_amount, '6': bet_amount}
        table = Table(initial_status)
        
        
        winning_bets = ['pass', '6']
        result = table.pay_bets(winning_bets)
        
        payout_for_6 = 7
        payout_for_pass = 6
        
        expected_result = payout_for_6 + payout_for_pass
        
        self.assertEqual(expected_result, result)

    def test_payout_double_bets(self):
        bet_amount = 12
        initial_status = copy(self.INITIAL_STATUS)
        initial_status['placed_bets'] = {'pass': bet_amount, '6': bet_amount}
        table = Table(initial_status)
        
        
        winning_bets = ['pass', '6']
        result = table.pay_bets(winning_bets)
        
        payout_for_6 = 14
        payout_for_pass = 12
        
        expected_result = payout_for_6 + payout_for_pass
        
        self.assertEqual(expected_result, result)

    def test_valid_pass_bets(self):
        expected_result = True
        
        table = Table()
        
        bet_amount = 1
        result = table.validate_bet('pass', bet_amount)
        self.assertEqual(expected_result, result)

        bet_amount = table.status()['bank']
        result = table.validate_bet('pass', bet_amount)
        self.assertEqual(expected_result, result)

        
    def test_invalid_pass_bets(self):
        expected_result = False
        
        table = Table()
        
        bet_amount = 0
        result = table.validate_bet('pass', bet_amount)
        self.assertEqual(expected_result, result)

        bet_amount = table.status()['bank'] + 1
        result = table.validate_bet('pass', bet_amount)
        self.assertEqual(expected_result, result)

        bet_amount = 'nonsense'
        result = table.validate_bet('pass', bet_amount)
        self.assertEqual(expected_result, result)

    def test_valid_number_bets(self):
        expected_result = True
        
        table = Table()
        number_bets = {
            '4' : 5,
            '5' : 5,
            '6' : 6,
            '8' : 6,
            '9' : 5,
            '10': 5
        }
        
        for bet in number_bets.keys():
            bet_amount = number_bets[bet]
            result = table.validate_bet(bet, bet_amount)
            self.assertEqual(expected_result, result)

        bet_amount = table.status()['bank']
        result = table.validate_bet('4', bet_amount)
        self.assertEqual(expected_result, result)

    def test_invalid_number_bets(self):
        expected_result = False
        
        table = Table()
        
        number_bets = {
            '4' : 5,
            '5' : 5,
            '6' : 6,
            '8' : 6,
            '9' : 5,
            '10': 5
        }
        
        for bet in number_bets.keys():
            for offset in [-1, 1]:
                bet_amount = number_bets[bet] + offset
                result = table.validate_bet(bet, bet_amount)
                self.assertEqual(expected_result, result)

        bet_amount = table.status()['bank'] + 1
        result = table.validate_bet('pass', bet_amount)
        self.assertEqual(expected_result, result)

        bet_amount = 'nonsense'
        result = table.validate_bet('pass', bet_amount)
        self.assertEqual(expected_result, result)



if __name__ == "__main__":
    unittest.main(verbosity=2)
