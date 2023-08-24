from apex.Helper.TopicFactory import TopicFactory


class Law_of_Cosines(TopicFactory):
    def __init__(self):

        self.input_dict = {
            "a": {
                "default_value": 14.62,
                "dimension": "length",
            },

            "b": {
                "default_value": 9,
                "dimension": "length",
            },

            "c": {
                "default_value": 12,
                "dimension": "length",
            },

            "A": {
                "default_value": None,
                "dimension": "angle",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": "a**2 == b**2 + c**2 - 2 * b * c * cos(A)",
             "Note": "This is the law of cosines",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info
