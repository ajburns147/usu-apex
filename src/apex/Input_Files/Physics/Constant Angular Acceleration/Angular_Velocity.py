from apex.Helper.TopicFactory import TopicFactory


class Angular_Velocity(TopicFactory):
    def __init__(self):

        g = 9.81


        self.input_dict = {
            "omega": {
                "default_value": 3,
                "dimension": "velocity",
            },

            "omegai": {
                "default_value": 5,
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
        }

        self.info = {
             "input": self.input_dict,
             "formula": f"omega == omegai * omegadot * time",
             "Note": """
                     This is the angular velocity of an object as a function of the initial angular velocity
                     and the angular acceleration
                     """,
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info