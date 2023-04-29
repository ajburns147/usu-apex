from apex.Helper.TopicFactory import TopicFactory


class Distance_in_y(TopicFactory):
    def __init__(self):

        g = 9.81

        self.input_dict = {
            "y": {
                "default_value": 3,
                "dimension": "length",
            },

            "yi": {
                "default_value": 4,
                "dimension": "length",
            },

            "time": {
                "default_value": 5,
                "dimension": "time",
            },

            "vyi": {
                "default_value": 3,
                "dimension": "velocity",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": f"y == yi + vyi * time - .5 * {g} * time**2",
             "Note": "This is the velocity of the projectile at any time",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info