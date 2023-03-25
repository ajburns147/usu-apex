from src.TopicFactory import TopicFactory


class pythagorean_theorem(TopicFactory):
    def __init__(self):
        self.input_dict = {
            "a": ["", "", 3],
            "b": ["", "", 4],
            "c": ["", "", 5],
                      }

        self.info = {
             "input": self.input_dict,
             "formula": "a**2 + b**2 == c**2",
             "Note": "This is Pythagoras's theorem",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus("")
             }

    def giveInfo(self):
        return self.info