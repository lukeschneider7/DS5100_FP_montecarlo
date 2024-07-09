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
            self.df = pd.DataFrame({'values': weights}, index=faces)    

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
            self.df.loc[face_to_change] = weight_new
            
    def roll_die(self, times=1):
        """ Roll die one or more times, returning outcomes
        Args:
            times: (int) times die is to be rolled
        Returns:
            outcomes: (list) Python list of outcomes not internally stored
        """
        self.outcomes = random.choices(self.df.index.tolist(), weights=self.df['values'], k=times)
        return self.outcomes
    
    def get_state(self):
        """ Returns a COPY of private die data frame
        """
        df_copy = self.df.copy()
        return df_copy
        

class Game():
    """ Rolling one or more similar die one or more times
    - Each die in a game have same num sides and associated faces, own weights
    - Initialize w/ list that has one or more dice
    - Only keep results of most recent play
    """
    def __init(self, similar_die):
        """ Takes list of alredy instantiated similar die
        Args:
            similar_die: (list) instantiated similar die"""
        self.similiar_die = similar_die

    def play(self, times_to_roll):
        """ Saves result of play to private df wide format 
        Args:
            times_to_roll (int) how many times die should be rolled
        """
        self.outcomes = Die.roll_die(times_to_roll) # list of outcomes 
        self.df_play = pd.DataFrame({'values': self.outcomes}, index= range(len(times_to_roll)), columns = range(len(self.similar_die)))
        
    def result(self, narrow_or_wide='wide'):
        """ Returns copy of private play() df to user
        - raise Value Error if user passes invalid argument
        Args:
            narrow_or_wide: (str) indicating df to be returned narrow or wide
        Returns:
            self._df_play: (dataframe) private df from play() method
        """
        if narrow_or_wide.lower() != 'narrow' and narrow_or_wide.lower() != 'wide':
            raise ValueError("specify 'narrow' or 'wide' df format to be returned")
        elif narrow_or_wide.lower() == 'narrow':
            self._df_play_narrow = pd.melt(self.df_play, id_vars=['roll number'], var_name='die number', value_name='face rolled')
            return self._df_play_narrow
        else:
            return self._df_play


class Analyszer():
    def __init(self, game_object):
        self.game_object = game_object

    def jackpot(self):
        pass
    def combo_count(self):
        pass
    def permutation_count(self):
        pass



