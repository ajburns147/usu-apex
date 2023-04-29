from apex.Helper.UnitFactory import UnitFactory

class acceleration(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "m/(s)^2": 1,
            "cm/(s)^2": .01,
            "in/(s)^2": 0.0254,
            "ft/(s)^2": 0.3048,
            "g_0": 9.80665
        }

    def giveDict(self):
        return self.unit_dict
