from apex.Helper.TopicFactory import TopicFactory


class Displacement_in_x(TopicFactory):
    def __init__(self):

        self.input_dict = {
            "x": {
                "default_value": 3,
                "dimension": "length",
            },

            "xi": {
                "default_value": 4,
                "dimension": "length",
            },

            "time": {
                "default_value": 5,
                "dimension": "time",
            },

            "vxi": {
                "default_value": 2,
                "dimension": "velocity",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": "x = xi + vxi * time",
             "Note": """
                     This is the distance that a projectile travels in the x direction as a function of initial
                     velocity, time and the initial position in x. 
                     """,
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info
