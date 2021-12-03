import unittest

# import the thing we're testing, without having to make a package
import diagnostics

fixture = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.split()

class Test3(unittest.TestCase):
    def test_gamma(self):
        self.assertEqual(diagnostics.diagnostics(fixture)[0],
        22)

    def test_epsilon(self):
        self.assertEqual(diagnostics.diagnostics(fixture)[1],
        9)

    def test_power(self):
        self.assertEqual(diagnostics.diagnostics(fixture)[2],
        198)

if __name__ == '__main__':
    unittest.main()