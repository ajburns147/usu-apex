from src.TopicFactory import TopicFactory


class Law_of_Cosines(TopicFactory):
    def __init__(self):
        self.input_dict = {
            "a": ["", 3, "length", "", ""],
            "b": ["", 4, "length", "", ""],
            "c": ["", 5, "length", "", ""],
            "A": ["", "", "length", "", ""]
        }

        self.info = {
             "input": self.input_dict,
             "formula": "a**2 == b**2 + c**2 - 2 * b * c * cos(A)",
             "Note": "This is the law of cosines",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus("")
             }

    def giveInfo(self):
        return self.info
