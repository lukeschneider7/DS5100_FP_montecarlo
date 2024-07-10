import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyszer
import unittest
from pandas.testing import assert_frame_equal


class DieTestCase(unittest.TestCase):
    def test_init_(self):
        weights = np.ones(die0.faces.size)
        faces = die0.faces.flatten()
        actual = die0.df
        expected = pd.DataFrame({'values': weights},
                                  index=faces)
        assert_frame_equal(actual, die0.df)


    def test_change_weight(self):
        i, weight = 5, 4
        die0.change_weight(i, weight)
        actual = die0.df.iloc[i-1]['values']
        expected = weight
        self.assertEqual(actual, expected)


    def test_roll_die(self):
        times = 3
        actual = len(die0.roll_die(times))
        expected = times
        self.assertEqual(actual, expected)


    def test_get_state(self):
        actual = die0.get_state()
        expected = die0.df
        assert_frame_equal(actual, expected)


class GameTestCase(unittest.TestCase):
    def test_init_(self):
        actual = game1.similar_dice_list
        expected = dice_list1
        self.assertEqual(actual, expected)

    def test_play(self):
        times_to_roll=3
        game1.play(times_to_roll)
        actual = game1.df_play.shape # Tuple of (nrows, ncolumns)
        expected = (times_to_roll, len(game1.similar_dice_list)) # Tuple of (times to roll, len(die_list))
        self.assertEqual(actual, expected)


    def test_result(self):
        times_to_roll=3
        game1.play(times_to_roll)
        actual = game1.result("narrow").shape # Tuple of narrow df
        expected = ((times_to_roll*len(dice_list1)), 3) # Tuple of nrows vs ncol df
        self.assertEqual(actual, expected)



class AnalyzerTestCase(unittest.TestCase):
    def test__init__ (self):
        pass
    def test_jackpot(self):
        pass
    def test_face_counts(self):
        pass
    def test_combo_count(self):
        pass
    def test_permutation_count(self):
        pass

if __name__ == '__main__':
    faces = np.array([[1, 2, 3],[4, 5, 6]])
    die0 = Die(faces)
    die1 = Die(faces)
    die2 = Die(faces)
    die1.change_weight(2, 10)
    die2.change_weight(3, 20)
    dice_list1 = [die0, die1, die2]
    game1 = Game(dice_list1)
    unittest.main()
