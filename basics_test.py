import unittest
import math
import random
import get_column_stats
import statistics


class TestColumnStats(unittest.TestCase):
    def test_mean_constant(self):
        # for constant test, generate an array [0 ... 99] and test its mean
        s = 0
        V = []
        for i in range(100):
            s += i
            V.append(i)
        self.assertEqual(get_column_stats.get_mean(V), 49.5)

    def test_stdev_constant(self):
        # for constant test, generate an array [0 ... 99] and test its stdev
        V = []
        for i in range(100):
            V.append(i)
        stdev = statistics.stdev(V)
        self.assertTrue(math.isclose(get_column_stats.get_stdev(V), stdev,
                                     rel_tol=10.0, abs_tol=0.0))

    def test_mean_random(self):
        # test 100 times to make the test more robust
        for _ in range(100):
            V = []
            # test array with 1000 random elements
            for _ in range(1000):
                r = random.randint(-1000, 1000)
                V.append(r)
            self.assertAlmostEqual(get_column_stats.get_mean(V),
                                   statistics.mean(V))

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
            self.assertTrue(math.isclose(get_column_stats.get_stdev(V),
                                         stdev, rel_tol=10.0, abs_tol=0.0))

    def test_list_mean_rand_float_model(self):
        V = []
        u = (0 + 100)/2.0
        for i in range(100):
            for j in range(10):
                V.append(random.uniform(0, 100))
            r = get_column_stats.get_mean(V)
            e = statistics.mean(V)
            self.assertTrue(math.isclose(r, u, rel_tol=10.0, abs_tol=0.0))

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
