from apex.Helper.TopicFactory import TopicFactory

from math import sin


class Projectile_Distance_in_x(TopicFactory):
    def __init__(self):

        g = 9.81

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
             "formula": f"xtot == (vi ** 2)/{g} * sin(2 * theta) ",
             "Note": """
                    This is the total distance travelled by the projectile in the x direction as a function 
                    of velocity, and angle. This is a special case where the starting and ending height must be
                    the same. 
                    """,
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info
