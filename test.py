import unittest
from table import Table

class TestTableIsOn(unittest.TestCase):

    def setUp(self):
        self.table = Table()
        
    def test_null(self):
        # if point is null then the table is off
        self.table.set_point()
        value = self.table.is_on
        self.assertEqual(value, False)
        
    def test_on(self):
        # if point is not null, the table is on
        self.table.set_point(4)
        value = self.table.is_on
        self.assertEqual(value, True)

class TestSetPoint(unittest.TestCase):
    
    def setUp(self):
        self.table = Table()

    def test_set_point_four(self):
        #point is valid if value is 4
        value = self.table.eval_roll(4)
        self.assertEqual(value, 4)

    def test_set_point_five(self):
        #point is valid if value is 5
        value = self.table.eval_roll(5)
        self.assertEqual(value, 5)

    def test_set_point_six(self):
        #point is valid if value is 6
        value = self.table.eval_roll(6)
        self.assertEqual(value, 6)

    def test_set_point_eight(self):
        #point is valid if value is 8
        value = self.table.eval_roll(8)
        self.assertEqual(value, 8)

    def test_set_point_nine(self):
        #point is valid if value is 9
        value = self.table.eval_roll(9)
        self.assertEqual(value, 9)

    def test_set_point_ten(self):
        #point is valid if value is 10
        value = self.table.eval_roll(10)
        self.assertEqual(value, 10)

    def test_set_point_two(self):
        #point is not valid if value is 2
        value = self.table.eval_roll(2)
        self.assertEqual(value, None)

    def test_set_point_three(self):
        #point is not valid if value is 3
        value = self.table.eval_roll(3)
        self.assertEqual(value, None)

    def test_set_point_two(self):
        #point is not valid if value is 2
        value = self.table.eval_roll(2)
        self.assertEqual(value, None)

    def test_set_point_three(self):
        #point is not valid if value is 3
        value = self.table.eval_roll(3)
        self.assertEqual(value, None)

    def test_set_point_seven(self):
        #point is not valid if value is 7
        value = self.table.eval_roll(7)
        self.assertEqual(value, None)

    def test_set_point_eleven(self):
        #point is not valid if value is 11
        value = self.table.eval_roll(11)
        self.assertEqual(value, None)

    def test_set_point_twelve(self):
        #point is not valid if value is 12
        value = self.table.eval_roll(12)
        self.assertEqual(value, None)

class TestRoll(unittest.TestCase):
    
    def setUp(self):
        self.table = Table()

    def test_roll_random(self):
        #test a randomly generated dice roll
        value1 = [self.table.roll_dice() for i in range(10)]
        value2 = [self.table.roll_dice() for i in range(10)]
        self.assertNotEqual(value1, value2)

class TestRollPoint(unittest.TestCase):
    
    def setUp(self):
        self.table = Table()

    def test_roll_valid_point_table_off(self):
        #test roll valid point with table off
        self.assertFalse(self.table.is_on)
        self.table.roll_dice = lambda: 4
        self.table.shoot()
        value = self.table.point
        self.assertEqual(value, 4)
        self.assertTrue(self.table.is_on)


    def test_roll_invalid_point_table_off(self):
        #test roll invalid point with table off
        self.assertFalse(self.table.is_on)
        self.table.roll_dice = lambda: 12
        self.table.shoot()
        value = self.table.point
        self.assertEqual(value, None)
        self.assertFalse(self.table.is_on)
        
    def test_roll_valid_point_table_on(self):
        #test roll with non-pass point  and non-craps with table on and point set
        self.table.eval_roll(9)
        self.assertTrue(self.table.is_on)
        self.table.roll_dice = lambda: 6
        self.table.shoot()
        value = self.table.point
        self.assertEqual(value, 9)
        self.assertTrue(self.table.is_on)

    def test_roll_craps_table_on(self):
        #test roll craps with table on and point set
        self.table.set_point(9)
        self.assertTrue(self.table.is_on)
        self.table.roll_dice = lambda: 7
        self.table.shoot()
        value = self.table.point
        self.assertEqual(value, None)
        self.assertFalse(self.table.is_on)


    def test_roll_pass_point_table_on(self):
        #test roll pass with table on and point set
        self.table.set_point(9)
        self.assertTrue(self.table.is_on)
        self.table.roll_dice = lambda: 9
        self.table.shoot()
        value = self.table.point
        self.assertEqual(value, None)
        self.assertFalse(self.table.is_on)


class TestPlaceBet(unittest.TestCase):
    
    def setUp(self):
        self.table = Table()

    def test_place_pass_bet(self):
        self.table.place_bet({'pass_line': 10})
        value = self.table.list_all_bets()
        self.assertEqual(value, {'pass_line': 10})
        
    def test_payout_pass_bet_10(self):
        self.table.place_bet({'pass_line': 10})
        self.table.set_point(9)
        self.assertTrue(self.table.is_on)
        self.table.roll_dice = lambda: 9
        value = self.table.payout(9)
        self.assertEqual(value, 20)

    def  test_payout_pass_bet_20(self):
        self.table.place_bet({'pass_line': 20})
        self.table.set_point(9)
        self.assertTrue(self.table.is_on)
        self.table.roll_dice = lambda: 9
        value = self.table.payout(9)
        self.assertEqual(value, 40)
        
    # def  test_payout_two_bets(self):
    #     self.table.place_bet({'pass_line': 20})
    #     self.table.place_bet({'non-point': 10})
    #     self.table.set_point(9)
    #     self.assertTrue(self.table.is_on)
    #     self.table.roll_dice = lambda: 9
    #     value = self.table.payout(9)
    #     self.assertEqual(value, 40)
        

class TestStatus(unittest.TestCase):
    
    def setUp(self):
        self.table = Table()
        self.default_status = {
            "is_on": False,
            "point": None,
            "placed_bets": {"pass_line": 10},
            "open_bets": [],
            "bank": 90
            }
            
    def test_initial_status_report(self):
        #Game Start - Table Off, No Point, No Bets, Initial Bank, Pass Line Available
        value = {}
        value = self.table.status()
        self.default_status.update({
                "placed_bets": {},
                "open_bets": ["pass_line"],
                "bank": 100                
                })
        self.assertEqual(value, self.default_status)

        
    def test_initial_status_report_first_bet(self):
        #First Bet - Table Off, No Point, Pass Bet - 10, Bank - 90, No Bets Available
        value = {}
        self.table.place_bet({'pass_line': 10})
        value = self.table.status()
        self.assertEqual(value, self.default_status)
        
    def test_initial_status_report_first_roll_craps(self):
        #Roll Craps - Table Off, No Point, Pass Bet - 0, Bank - 90, Pass Bet Available
        value = {}
        self.table.place_bet({'pass_line': 10})
        self.table.roll_dice = lambda: 2
        self.table.shoot()
        value = self.table.status()
        self.default_status.update({
                "placed_bets": {},
                "open_bets": ["pass_line"]
                })
        self.assertEqual(value, self.default_status)
        
    def test_initial_status_report_first_roll_pass(self):
        #Roll Pass - Table Off, No Point, Pass Bet - 10, Bank - 100
        value = {}
        self.table.place_bet({'pass_line': 10})
        self.table.roll_dice = lambda: 7
        self.table.shoot()
        value = self.table.status()
        self.default_status.update({
                "bank": 100                
                })
        self.assertEqual(value, self.default_status)

    def test_initial_status_report_first_roll_point(self):
        #Roll Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
        value = {}
        self.table.place_bet({'pass_line': 10})
        self.table.roll_dice = lambda: 6
        self.table.shoot()
        value = self.table.status()
        self.default_status.update({
                "is_on": True,
                "point": 6,
                "open_bets": ["non_point"],
                })
        self.assertEqual(value, self.default_status)

    def test_initial_status_report_bet_non_point(self):
        #Bet Non_Point - Table On, Point = Roll, Pass Bet - 10, Bank - 90
        value = {}
        self.table.place_bet({'pass_line': 10})
        self.table.roll_dice = lambda: 6
        self.table.shoot()
        self.table.place_bet({'non_point': 15})
        value = self.table.status()
        self.default_status.update({
                "is_on": True,
                "point": 6,
                "placed_bets": {"pass_line": 10, "non_point": 15},
                "bank": 75
                })
        self.assertEqual(value, self.default_status)
        
if __name__ == '__main__':
    unittest.main(verbosity = 2)
