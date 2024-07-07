import numpy as np
import pandas as pd


class Die():
    def __init__(self, faces):
        """ 
        -1. Throw TypeError if not NumPy array, raise ValueError if array values not distinct
        -3. Internally initialize weights to 1.0 for each face
        -4. Save faces and weights in private df w/ faces in index
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
            print(self.df)
        

    def change_weight(self, face_to_change, weight_new ):
        """Change weight of single die
        - Raise IndexError if face_value not in die array
        - Raise TypeError if weight_new is not valid type (int/float or castable as numeric)
        Args:
            face_to_change = face value to change
            weight_new = (str/int/float) new weight for face
        """
        if np.isin(face_to_change, self.faces)==False:
            raise IndexError("Face value not in die array")
        
        elif type(weight_new)!=float and int(weight_new)!= True and type(weight_new)!=int:
            raise TypeError("Weight_new arg must be int/float or castable as num")
        
        else:
            self.df.loc[face_to_change] = weight_new
            print(self.df)
        

    def roll_die(self, times=1):
        """Roll die one or more times
        Args:
            times: (int) times die is to be rolled
        Returns:
            outcomes: (list) Python list of outcomes
        """
        pass
    

    def get_state(self):
        pass
        


class Game():
    def __init(self):
        pass



class Analyszer():
    def __init(self):
        pass



array = np.random.randint(0, 40, size=(2, 3))
print(array)
die = Die(array)
die.change_weight(7, 'four')