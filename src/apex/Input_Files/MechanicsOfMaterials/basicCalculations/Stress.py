from apex.Helper.TopicFactory import TopicFactory


class Stress(TopicFactory):
    def __init__(self):

        self.input_dict = {
            "F": {
                "default_value": 3,
                "dimension": "length",
            },

            "A": {
                "default_value": 4,
                "dimension": "length",
            },

            "stress": {
                "default_value": None,
                "dimension": "length",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": "stress == F/A",
             "Note": "This is a stress calculator",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info
