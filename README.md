# DS5100-FP1

# Project Description 

This project is a montecarlo Die game Simulator

-   **Metadata**: 
Name: Luke Schneider
Project Name: Montecarlo Simulator



-   **Synopsis:** Show brief demo code of how the classes are used, i.e.
    code snippets showing how to install, import, and use the code
    to (1) create dice, (2) play a game, and (3) analyze a game. You can
    use preformatted blocks for the code.

-   Intstall: 
    To install the package, navigate to the directory containing `setup.py` and run the following in the terminal:

```bash
pip install .
```
-   Import: 
    To Import the montecarlo file from the montecarlo package run the following with a python interpreter:

```python
from montecarlo import montecarlo
```

- (1) Create dice:
    - Create a numpy array of faces
    - instantiate die object with faces as arg, weights all = 1
    - can change weight with args of (face, weight)

```python
faces =  np.array([1, 2, 3, 4, 5, 6])
die1 = montecarlo.Die(faces)
die1.change_weight(5, 4)
```

- (2) Play Game:
    - create a dice list of die with similar faces, can have different weights or same
    - instantiate game object with dice_list as arg
    - "play" game object with arg of times to roll

```python
dice_list = [die1] * 3
game1 = montecarlo.Game(dice_list)
game1.play(times to roll)
```

- (3) Analyze Game: 
    - create Analzyer object with arg of game object
    - jackpot method counts rolls where all faces are same
    - face_count method counts number of times face rolled in event
    - combination and permuation counters
```python
analyze1 = Analyzer(game1)
analzye1.jackpot()
analyze1.combo_count()
analyze1.permutation_count()
```



-   **API description**: A list of all classes with their public methods
    and attributes. Each item should show their docstrings. All
    parameters (with data types and defaults) should be described. All
    return values should be described. Do not describe private methods
    and attributes.

    class Die():
    """Initialize a die with faces given as a numpy array and a weight for each face
    - Include methods for changing weights, rolling die, and returning die df
    """
    def \__init\__(self, faces):
        """ Internally initialize weights to 1 for each face
        - Throw TypeError if not NumPy array, raise ValueError if array values not distinct
        - Save faces and weights in private df w/ faces in index
        Args:
            faces: (array) NumPy array faces str/num dtype
        """

    def change_weight(self, face_to_change, weight_new ):
        """ Change weight of single face of die
        - Raise IndexError if face_value not in die array
        - Raise TypeError if weight_new is not valid type (int/float or castable as numeric)
        Args:
            face_to_change = face value to change
            weight_new = (str/int/float) new weight for face
        """

    def roll_die(self, times=1):
        """ Roll die one or more times, returning outcomes
        Args:
            times: (int) times die is to be rolled
        Returns:
            outcomes: (list) Python list of outcomes not internally stored
        """

    def get_state(self):
        """ Returns a COPY of private die data frame
        """
        

class Game():
    """ Rolling one or more similar die one or more times
    - Each die in a game have same num sides and associated faces, own weights
    - Initialize w/ list that has one or more dice
    - Only keep results of most recent play
    """
    def \__init\__(self, dice_list):
        """ Takes list of alredy instantiated similar die
        Args:
            similar_die: (list) instantiated similar die"""


    def play(self, times_to_roll):
        """Saves result of play to private df wide format 
        Args:
            times_to_roll (int) how many times die should be rolled
        """

    def result(self, narrow_or_wide='wide'):
        """Returns copy of private play() df to user, raise ValueError if invalid arg
        Args:
            narrow_or_wide: (str) indicating df to be returned narrow or wide
        Returns:
            copy_df : (dataframe) copy of private df from play() method
        """


class Analyzer():
    """Takes results of a single game and computes descriptive stats about it
    """
    def \__init\__(self, game_object):
        """Instantiates a Game object, throws value error if not passed game object
        Args:
            game_object: a game object 
        """
  


    def jackpot(self):
        """Computes how many times a game results in jackpot(all faces same)
        Returns:
            jackpots: (int) integer for number of jackpots
        """

    def face_counts(self):
        """Computes how many times a given face is rolled in each event
        Returns:
            face_count: (DataFrame) index roll number, faces for columns, counts as values in cells
        """

    def combo_count(self):
        """Computes distinct combinations of faces rolled along with counts
        Returns:
            combo_counts: (DataFrame) multiindex of distinct combos and column for associated counts
        """

    def permutation_count(self):
        """Computes distinct permutations of faces rolled, along with counts
        Returns:
            permu_count: (DataFrame) mutltiindex of distinct permutations and column for associated counts
        """
    
