import unittest
import math
import random
import get_column_stats


class TestColumnStats(unittest.TestCase):
    def test_mean_constant(self):
        # for constant test, generate an array [0 ... 99] and test its mean
        s = 0
        V = []
        for i in range(100):
            s += i
            V.append(i)
        self.assertEqual(get_column_stats.get_mean(V), s/len(V))

    def test_stdev_constant(self):
        # for constant test, generate an array [0 ... 99] and test its stdev
        s = 0
        V = []
        for i in range(100):
            s += i
            V.append(i)
        mean = s/len(V)
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
        self.assertEqual(get_column_stats.get_stdev(V), stdev)

    def test_mean_random(self):
        # test 100 times to make the test more robust
        for _ in range(100):
            V = []
            s = 0
            # test array with 1000 random elements
            for _ in range(1000):
                r = random.randint(-1000, 1000)
                V.append(r)
                s += r
            self.assertEqual(get_column_stats.get_mean(V), s/len(V))

    def test_stdev_random(self):
        # test 100 times to make the test more robust
        for _ in range(100):
            V = []
            s = 0
            # test array with 1000 random elements
            for _ in range(1000):
                r = random.randint(-1000, 1000)
                V.append(r)
                s += r
            mean = s/len(V)
            stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
            self.assertEqual(get_column_stats.get_stdev(V), stdev)

    def test_empty_array(self):
        # use empty array to test get_column_stats
        # should return None
        V = []
        self.assertIsNone(get_column_stats.get_mean(V))
        self.assertIsNone(get_column_stats.get_stdev(V))

    def test_dirty_list(self):
        # use array containing string, boolean, and numbers to test
        # should return None
        V = ['abc', 123, 0.1111, 'ww', 'hey', True]
        self.assertIsNone(get_column_stats.get_mean(V))
        self.assertIsNone(get_column_stats.get_stdev(V))


if __name__ == '__main__':
    unittest.main()
