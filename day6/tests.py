import unittest

from lantern import breeding, num_doublings


class TestLantern(unittest.TestCase):
    def test_num_doublings(self):
        self.assertEqual(num_doublings(2, 1), 0)
        self.assertEqual(num_doublings(2, 2), 0)
        self.assertEqual(num_doublings(2, 3), 1)
        self.assertEqual(num_doublings(2, 3), 1)

    def test_count_down_consecutive(self):
        self.assertEqual(
            day(line_to_counts('3,2')),
                line_to_counts('2,1'))

    def test_count_downs(self):
        self.assertEqual(
            day(line_to_counts('3,4,3,1,2')),
                line_to_counts('2,3,2,0,1'))

    def test_spawn(self):
        self.assertEqual(
            day(line_to_counts('0')),
                line_to_counts('6,8'))

    def test_examples(self):
        examples = '''
2,3,2,0,1
1,2,1,6,0,8
0,1,0,5,6,7,8
6,0,6,4,5,6,7,8,8
5,6,5,3,4,5,6,7,7,8
4,5,4,2,3,4,5,6,6,7
3,4,3,1,2,3,4,5,5,6
2,3,2,0,1,2,3,4,4,5
1,2,1,6,0,1,2,3,3,4,8
0,1,0,5,6,0,1,2,2,3,7,8
6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
'''.strip().split()
        examples = [line_to_counts(line) for line in examples]
        initial_fish_timer_counts = examples[0]
        for num_days, today in enumerate(examples):
            self.assertEqual(breeding(initial_fish_timer_counts, num_days), today.total())

if __name__ == '__main__':
    unittest.main()