import unittest
from table import Table

class TestGameIntegration(unittest.TestCase):

    def setUp(self):
        self.table = Table()

    def test_winning_streak(self):
        status = self.table.status()
        self.assertEqual(status['bank'], 100)
        self.table.place_bet({"pass_line": 20})
        self.table.roll_dice = lambda: 7
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 100)
        self.assertEqual(status['placed_bets'], {"pass_line": 20})
        self.table.roll_dice = lambda: 11
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 120)
        self.assertEqual(status['placed_bets'], {"pass_line": 20})
        self.table.roll_dice = lambda: 8
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 120)
        self.assertEqual(status['placed_bets'], {"pass_line": 20})
        self.table.roll_dice = lambda: 8
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 140)
        self.assertEqual(status['placed_bets'], {"pass_line": 20})


    def test_losing_streak(self):
        status = self.table.status()
        self.assertEqual(status['bank'], 100)
        self.table.place_bet({"pass_line": 20})
        self.table.roll_dice = lambda: 2
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 80)
        self.assertEqual(status['placed_bets'], {})
        self.table.place_bet({"pass_line": 20})
        self.table.roll_dice = lambda: 3
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 60)
        self.assertEqual(status['placed_bets'], {})
        self.table.place_bet({"pass_line": 20})
        self.table.roll_dice = lambda: 12
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 40)
        self.assertEqual(status['placed_bets'], {})
        self.table.place_bet({"pass_line": 20})
        self.table.roll_dice = lambda: 8
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 20)
        self.assertEqual(status['placed_bets'], {"pass_line": 20})
        self.table.roll_dice = lambda: 7
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 20)
        self.assertEqual(status['placed_bets'], {})

    def test_over_bet(self):
        status = self.table.status()
        self.assertEqual(status['bank'], 100)
        bet_status = self.table.place_bet({"pass_line": 120})
        self.table.roll_dice = lambda: 2
        self.table.shoot()
        status = self.table.status()
        self.assertEqual(status['bank'], 100)
        self.assertEqual(status['placed_bets'], {})
        self.assertFalse(bet_status)

        
if __name__ == '__main__':
    unittest.main(verbosity = 2)
