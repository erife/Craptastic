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
    
    def test_initial_status(self):
        table = Table()
        expected_result = self.INITIAL_STATUS
        
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
        
        expected_result = copy(self.INITIAL_STATUS)
        expected_result['is_on'] = True
        table.set_on()
        
        result = table.status()
        self.assertEqual(expected_result, result)
 

 
    def test_set_status_off(self):
        initial_status = copy(self.INITIAL_STATUS)
        initial_status['is_on'] = True
        table = Table(initial_status)
 
        expected_result = self.INITIAL_STATUS
        table.set_off()
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
    def test_increment_bank(self):
        table = Table()
        
        expected_result = copy(self.INITIAL_STATUS)
        expected_result['bank'] = 101
 
        table.increment_bank(1)
        
        result = table.status()
        self.assertEqual(expected_result, result)
 
    def test_decrement_bank(self):
        table = Table()
        
        expected_result = copy(self.INITIAL_STATUS)
        expected_result['bank'] = 99
 
        table.decrement_bank(1)
        
        result = table.status()
        self.assertEqual(expected_result, result)


    def test_place_bet(self):
        table = Table()
        
        expected_result = copy(self.INITIAL_STATUS)
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
                
 
 

        
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
    
    
