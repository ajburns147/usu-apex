from apex.Helper.TopicFactory import TopicFactory


class Velocity_in_y(TopicFactory):
    def __init__(self):

        g = 9.81

        self.input_dict = {
            "vy": {
                "default_value": 3,
                "dimension": "velocity",
            },

            "vyi": {
                "default_value": 4,
                "dimension": "velocity",
            },

            "time": {
                "default_value": 5,
                "dimension": "time",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": f"vy == vyi - {g} * time",
             "Note": "This is the velocity of the projectile at any time",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info