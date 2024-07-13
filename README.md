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