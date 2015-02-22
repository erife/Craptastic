import unittest
from table import Table

class TestTableIsOn(unittest.TestCase):

    def setUp(self):
        self.table = Table()
        
    def test_null(self):
        # if point is null then the table is off
        self.table.set_point()
        value = self.table.is_on()
        self.assertEqual(value, False)
        
    def test_on(self):
        # if point is not null, the table is on
        self.table.set_point(4)
        value = self.table.is_on()
        self.assertEqual(value, True)

class TestSetPoint(unittest.TestCase):
    
    def setUp(self):
        self.table = Table()

    def test_set_point_four(self):
        #point is valid if value is 4
        value = self.table.set_point(4)
        self.assertEqual(value, 4)

    def test_set_point_five(self):
        #point is valid if value is 5
        value = self.table.set_point(5)
        self.assertEqual(value, 5)

    def test_set_point_six(self):
        #point is valid if value is 6
        value = self.table.set_point(6)
        self.assertEqual(value, 6)

    def test_set_point_eight(self):
        #point is valid if value is 8
        value = self.table.set_point(8)
        self.assertEqual(value, 8)

    def test_set_point_nine(self):
        #point is valid if value is 9
        value = self.table.set_point(9)
        self.assertEqual(value, 9)

    def test_set_point_ten(self):
        #point is valid if value is 10
        value = self.table.set_point(10)
        self.assertEqual(value, 10)

    def test_set_point_two(self):
        #point is not valid if value is 2
        value = self.table.set_point(2)
        self.assertEqual(value, None)

    def test_set_point_three(self):
        #point is not valid if value is 3
        value = self.table.set_point(3)
        self.assertEqual(value, None)

    def test_set_point_two(self):
        #point is not valid if value is 2
        value = self.table.set_point(2)
        self.assertEqual(value, None)

    def test_set_point_three(self):
        #point is not valid if value is 3
        value = self.table.set_point(3)
        self.assertEqual(value, None)

    def test_set_point_seven(self):
        #point is not valid if value is 7
        value = self.table.set_point(7)
        self.assertEqual(value, None)

    def test_set_point_eleven(self):
        #point is not valid if value is 11
        value = self.table.set_point(11)
        self.assertEqual(value, None)

    def test_set_point_twelve(self):
        #point is not valid if value is 12
        value = self.table.set_point(12)
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
        self.assertFalse(self.table.is_on())
        self.table.roll_dice = lambda: 4
        value = self.table.shoot()
        self.assertEqual(value, 4)
        self.assertTrue(self.table.is_on())
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTableIsOn)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSetPoint)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRoll)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRollPoint)
    unittest.TextTestRunner(verbosity = 2).run(suite)
