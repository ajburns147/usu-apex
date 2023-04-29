from apex.Helper.TopicFactory import TopicFactory
import numpy as np

class Orbital_Period(TopicFactory):
    def __init__(self):

        G = 6.6743 * np.power(10.0, -11)

        self.input_dict = {
            "orbitalradius": {
                "default_value": 3,
                "dimension": "length",
            },

            "massorbitant": {
                "default_value": 4,
                "dimension": "mass",
            },

            "time": {
                "default_value": 5,
                "dimension": "time",
            },

            "orbitalperiod": {
                "default_value": 3,
                "dimension": "time",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": f"orbitalperiod == np.sqrt((4 * np.pi**2 * np.power(orbitalradius, 3) / {G} * massorbitant)",
             "Note": """This is the orbital period of an object around a celestial body as a function of radius and mass
                        """,
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info