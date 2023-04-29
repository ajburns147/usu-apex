from apex.Helper.TopicFactory import TopicFactory

from math import cos


class Initial_Velocity_in_x(TopicFactory):
    def __init__(self):

        g = 9.81

        self.input_dict = {
            "vxi": {
                "default_value": 3,
                "dimension": "velocity",
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
             "formula": f"vxi == vi * cos(theta)",
             "Note": """
                    This is the initial velocity in x as a function of the initial velocity and the angle of 
                    projection
                    """,
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info
