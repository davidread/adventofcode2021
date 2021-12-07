import unittest

import main

class TestLeastFuelPart1(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(main.calc_least_fuel_part1([1, 2, 3]),
                         (2, 2))

    def test_example(self):
        self.assertEqual(main.calc_least_fuel_part1(main.str_to_ints('16,1,2,0,4,2,7,1,2,14')),
                         (2, 37))


class TestLeastFuelPart2(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(main.calc_least_fuel_part2([1, 2, 3]),
                         (2, 2))

    def test_example(self):
        self.assertEqual(main.calc_least_fuel_part2(main.str_to_ints('16,1,2,0,4,2,7,1,2,14')),
                         (5, 168))


if __name__ == '__main__':
    unittest.main()