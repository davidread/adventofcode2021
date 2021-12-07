import unittest

import main

class TestLeastFuel(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(main.calc_least_fuel([1, 2, 3]),
                         (2, 2))

    def test_example(self):
        self.assertEqual(main.calc_least_fuel(main.str_to_ints('16,1,2,0,4,2,7,1,2,14')),
                         (2, 37))


if __name__ == '__main__':
    unittest.main()