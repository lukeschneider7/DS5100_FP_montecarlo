import numpy as np
import pandas as pd
import random


class Die():
    """Initialize a die with faces given as a numpy array and a weight for each face
    - Include methods for changing weights, rolling die, and returning die df
    """
    def __init__(self, faces):
        """ Internally initialize weights to 1 for each face
        - Throw TypeError if not NumPy array, raise ValueError if array values not distinct
        - Save faces and weights in private df w/ faces in index
        Args:
            faces: (array) NumPy array faces str/num dtype
        """
        self.faces = faces
        if not isinstance(faces, np.ndarray): 
            raise TypeError("Faces given not a NumPy array")
        elif faces.size != np.unique(faces).size: 
            raise ValueError("Array values not unique")
        else: 
            weights = np.ones(faces.size)
            faces = faces.flatten()
            self._df = pd.DataFrame({'values': weights}, index=faces)    


    def change_weight(self, face_to_change, weight_new ):
        """ Change weight of single face of die
        - Raise IndexError if face_value not in die array
        - Raise TypeError if weight_new is not valid type (int/float or castable as numeric)
        Args:
            face_to_change = face value to change
            weight_new = (str/int/float) new weight for face
        """
        if np.isin(face_to_change, self.faces)==False:
            raise IndexError("Face value not in die array")
        elif type(float(weight_new))!= float:
            raise TypeError("Weight_new arg must be int/float or castable as num")
        else:
            self._df.loc[face_to_change] = weight_new


    def roll_die(self, times=1):
        """ Roll die one or more times, returning outcomes
        Args:
            times: (int) times die is to be rolled
        Returns:
            outcomes: (list) Python list of outcomes not internally stored
        """
        outcomes = random.choices(self._df.index.tolist(), weights=self._df['values'], k=times)
        return outcomes
    

    def get_state(self):
        """ Returns a COPY of private die data frame
        """
        df_copy = self._df.copy()
        return df_copy
        


class Game():
    """ Rolling one or more similar die one or more times
    - Each die in a game have same num sides and associated faces, own weights
    - Initialize w/ list that has one or more dice
    - Only keep results of most recent play
    """
    def __init__(self, dice_list):
        """ Takes list of alredy instantiated similar die
        Args:
            similar_die: (list) instantiated similar die"""
        self.similar_dice_list = dice_list


    def play(self, times_to_roll):
        """Saves result of play to private df wide format 
        Args:
            times_to_roll (int) how many times die should be rolled
        """
        outcomes = list()
        self.times_to_roll = times_to_roll
        for die in self.similar_dice_list:
            outcomes.append(die.roll_die(times_to_roll)) # list of outcomes 
        self._df_play = pd.DataFrame(index= range(1, times_to_roll+1), 
                                    columns = range(len(self.similar_dice_list)))
        self._df_play[:] = [[outcomes[i][j] for i in range(len(outcomes))] for j in range(len(outcomes[0]))]
    

    def result(self, narrow_or_wide='wide'):
        """Returns copy of private play() df to user, raise ValueError if invalid arg
        Args:
            narrow_or_wide: (str) indicating df to be returned narrow or wide
        Returns:
            copy_df : (dataframe) copy of private df from play() method
        """
        self.copy_df = self._df_play.copy()
        if narrow_or_wide.lower() != 'narrow' and narrow_or_wide.lower() != 'wide':
            raise ValueError("specify 'narrow' or 'wide' df format to be returned")
        elif narrow_or_wide.lower() == 'narrow':
            self.copy_df = pd.melt(self.copy_df.reset_index(), id_vars=['index'], var_name='variable', value_name='value')
            self.copy_df.rename(columns={'index': 'roll',
                                         'variable': 'die',
                                         'value': 'face' }, inplace=True)
            return self.copy_df
        else:
            return self.copy_df



class Analyzer():
    """Takes results of a single game and computes descriptive stats about it
    """
    def __init__(self, game_object):
        """Instantiates a Game object, throws value error if not passed game object
        Args:
            game_object: a game object 
        """
        if isinstance(game_object, Game) == False:
            raise ValueError('Analzyer object not instantiated with a game object')
        self.game_object = game_object


    def jackpot(self):
        """Computes how many times a game results in jackpot(all faces same)
        Returns:
            jackpots: (int) integer for number of jackpots
        """
        jackpots = 0
        df_narrow = self.game_object.result(narrow_or_wide='narrow')

        for i in range(1, self.game_object.times_to_roll+1):
            faces_each_die = df_narrow.loc[df_narrow['roll'] == i, ['face']]
            if len(faces_each_die['face'].unique()) == 1:
                jackpots += 1
        return jackpots


    def face_counts(self):
        """Computes how many times a given face is rolled in each event
        Returns:
            face_count: (DataFrame) index roll number, faces for columns, counts as values in cells
        """
        result = self.game_object.result(narrow_or_wide='wide')

        face_count = pd.DataFrame(0, index=range(1, self.game_object.times_to_roll+1) ,
                                   columns=self.game_object.similar_dice_list[0].faces)
        
        for i in result.index: # Use roll i(1,2,3)
            counts = result.loc[i].value_counts() # Count num of each face in i row
            face_count.loc[i, counts.index] = counts # Fill in i row, and counts.index(a face) column with counts data
        return face_count


    def combo_count(self):
        """Computes distinct combinations of faces rolled along with counts
        Returns:
            combo_counts: (DataFrame) multiindex of distinct combos and column for associated counts
        """
        result = self.game_object.result(narrow_or_wide='wide')
        sorted_combos = result.apply(lambda x: tuple(sorted(x)), axis=1)
        combo_counts = sorted_combos.value_counts().rename_axis('Distinct Face Combos').reset_index(name='Count')
        combo_counts.set_index('Distinct Face Combos', inplace=True)
        combo_counts
        return combo_counts


    def permutation_count(self):
        """Computes distinct permutations of faces rolled, along with counts
        Returns:
            permu_count: (DataFrame) mutltiindex of distinct permutations and column for associated counts
        """
        result = self.game_object.result(narrow_or_wide='wide')
        face_combos = result.apply(tuple, axis=1)
        face_counts = face_combos.value_counts()
        permu_counts = face_counts.rename_axis('Distinct Face Permutations').reset_index(name='Count')
        permu_counts.set_index('Distinct Face Permutations', inplace=True)
        permu_counts
        return permu_counts
