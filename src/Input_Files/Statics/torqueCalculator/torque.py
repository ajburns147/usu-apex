from TopicFactory import TopicFactory

class torque(TopicFactory):
    def __init__(self):
        self.input_dict = {
            "F": ["", 1, "length", "", ""],
            "r": ["", 2, "length", "", ""],
            "Torque": ["", "", "length", "", ""],
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
