from apex.Helper.TopicFactory import TopicFactory


class Angular_Acceleration(TopicFactory):
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

            "omegadoti": {
                "default_value": 3,
                "dimension": "acceleration",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": f"omegadot ** 2 == omegadoti ** 2 + 2 * omegadot * (radialposition - radialpositioni)",
             "Note": """
                     This is the angular acceleration of an object as a function of angular acceleration and 
                     angular velocity.
                     """,
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info