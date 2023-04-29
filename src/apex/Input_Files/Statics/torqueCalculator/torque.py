from apex.Helper.TopicFactory import TopicFactory

class torque(TopicFactory):
    def __init__(self):
        self.input_dict = {
            "F": {
                "default_value": 1,
                "dimension": "length",
            },

            "r": {
                "default_value": 2,
                "dimension": "length",
            },

            "Torque": {
                "default_value": None,
                "dimension": "length",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": "Torque == r*F",
             "Note": "This is a one dimensional torque calculator",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info
