import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyszer
import unittest
from pandas.testing import assert_frame_equal

class DieTestCase(unittest.TestCase): 
    def test_change_weight(self):
        array = np.array([[1, 2, 3],[4, 5, 6]])
        die = Die(array)
        i, weight = 5, 4
        die.change_weight(i, weight)
        actual = die.df.iloc[i-1]['values']
        expected = weight
        self.assertEqual(actual, expected)

    def test_roll_die(self):
        array = np.array([[1, 2, 3],[4, 5, 6]])
        die = Die(array)
        i, weight = 5, 4
        die.change_weight(i, weight)
        times = 3
        die.roll_die(times)
        actual = len(die.outcomes)
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_get_state(self):
        actual = die.get_state()
        expected = die.df
        assert_frame_equal(actual, expected)


class GameTestCase(unittest.TestCase):
    def test_play(self):
        pass
    def test_result(self):
        pass
        

class AnalyzerTestCase(unittest.TestCase):
    def test_jackpot(self):
        pass
    def test_combo_count(self):
        pass
    def test_permutation_count(self):
        pass

if __name__ == '__main__':
    array = np.array([[1, 2, 3],[4, 5, 6]])
    die = Die(array)
    i, weight = 5, 4
    unittest.main()
