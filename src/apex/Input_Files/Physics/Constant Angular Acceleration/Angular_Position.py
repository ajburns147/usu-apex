from apex.Helper.TopicFactory import TopicFactory


class Angular_Position(TopicFactory):
    def __init__(self):

        g = 9.81

        self.input_dict = {
            "radialposition": {
                "default_value": 3,
                "dimension": "angle",
            },

            "omegai": {
                "default_value": 4,
                "dimension": "velocity",
            },

            "time": {
                "default_value": 5,
                "dimension": "time",
            },

            "omegadot": {
                "default_value": 3,
                "dimension": "acceleration",
            },

            "radialpositioni": {
                "default_value": 2,
                "dimension": "angle",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": f"radialposition == radialpositioni +  omegai * time + .5 * omegadot * time ** 2",
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