from apex.Helper.UnitFactory import UnitFactory

class velocity(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "m/s": 1,
            "cm/s": .01,
            "ft/s": 0.3048,
            "ft/min": 0.00508,
            "km/h": 0.2777777777777778,
            "mph": 0.44704,
            "knot": 0.514444444,
        }

    def giveDict(self):
        return self.unit_dict
