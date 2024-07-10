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
        outcomes = random.choices(self.df.index.tolist(), weights=self.df['values'], k=times)
        return outcomes
    

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
    def __init__(self, dice_list):
        """ Takes list of alredy instantiated similar die
        Args:
            similar_die: (list) instantiated similar die"""
        self.similar_dice_list = dice_list


    def play(self, times_to_roll):
        """ Saves result of play to private df wide format 
        Args:
            times_to_roll (int) how many times die should be rolled
        """
        outcomes = list()
        for die in self.similar_dice_list:
            outcomes.append(die.roll_die(times_to_roll)) # list of outcomes 
        print(outcomes)
        self.df_play = pd.DataFrame(index=range(1, times_to_roll+1), 
                                    columns = range(len(self.similar_dice_list)))
        self.df_play[:] = [[outcomes[i][j] for j in range(len(outcomes[0]))] for i in range(len(outcomes))]


    def result(self, narrow_or_wide='wide'):
        """ Returns copy of private play() df to user
        - raise Value Error if user passes invalid argument
        Args:
            narrow_or_wide: (str) indicating df to be returned narrow or wide
        Returns:
            self._df_play: (dataframe) private df from play() method
        """
        copy_df = self.df_play.copy()
        if narrow_or_wide.lower() != 'narrow' and narrow_or_wide.lower() != 'wide':
            raise ValueError("specify 'narrow' or 'wide' df format to be returned")
        elif narrow_or_wide.lower() == 'narrow':
            self.df_play_narrow = pd.melt(copy_df, id_vars=['roll number'], var_name='die number', value_name='face rolled')
            return self.df_play_narrow
        else:
            return copy_df


class Analyszer():
    def __init(self, game_object):
        #if type(game_object) != type()
        # raise ValueError("game_object arg given not a game object")
        #else:
            #self.game_object = game_object
        pass
    def jackpot(self):
        pass
    def face_counts(self):
        pass
    def combo_count(self):
        pass
    def permutation_count(self):
        pass

  

    faces = np.array([[1, 2, 3],[4, 5, 6]])
    die0 = Die(faces)
    die1 = Die(faces)
    die2 = Die(faces)
    die1.change_weight(2, 10)
    die2.change_weight(3, 20)
    dice_list = [die0, die1, die2]

    game1 = Game(dice_list)
    game1.play(times_to_roll=3)
    print(game1.result(narrow_or_wide='wide'))
    
    #analyze1 = Analyszer(game1)
    