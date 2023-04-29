from apex.Helper.TopicFactory import TopicFactory
import numpy as np


class Escape_Velocity(TopicFactory):
    def __init__(self):

        G = 6.6743 * np.power(10, -11)

        self.input_dict = {
            "vesc": {
                "default_value": 3,
                "dimension": "velocity",
            },

            "massorbitant": {
                "default_value": 4,
                "dimension": "mass",
            },

            "time": {
                "default_value": 5,
                "dimension": "time",
            },

            "radius": {
                "default_value": 3,
                "dimension": "length",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": f"vesc == np.sqrt((2 * {G} * massorbitant) / radius)",
             "Note": """
                     This is the angular position as a function of initial position, angular velocity, 
                     and angular acceleration.
                     """,
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info
