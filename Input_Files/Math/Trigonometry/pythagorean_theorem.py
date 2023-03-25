from src import TopicFactory

class Pyhagoreantheorem(TopicFactory):
    def __init__(self):
        self.input_dict = {"a": ["", "", 3],
                      "b": ["", "", 4],
                      "c": ["", "", 5],
                      }

        self.info = {
             "input": self.input_dict,
             "formula": "a**2 + b**2 == c**2",
             "Note": "This is Pythagoras's theorem",
             "solve_method": "",
             "plot_method": False,
             "Bonus" : "Bonus"
             }



    def giveInfo(self):
        return self.inf