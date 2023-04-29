from apex.Helper.TopicFactory import TopicFactory

from math import cos


class Projectile_Distance_in_x(TopicFactory):
    def __init__(self):

        self.input_dict = {
            "xtot": {
                "default_value": 3,
                "dimension": "length",
            },

            "vi": {
                "default_value": 4,
                "dimension": "velocity",
            },

            "time": {
                "default_value": 5,
                "dimension": "time",
            },

            "theta": {
                "default_value": 3,
                "dimension": "angle",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": "xtot == vi * cos(theta) * time",
             "Note": """
                    This is the total distance travelled by the projectile in 
                    the x direction as a function of velocity, angle, and time
                    """,
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info
