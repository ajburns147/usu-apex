from apex.Helper.UnitFactory import UnitFactory

class force(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "N": 1,
            "kN": 1e3,
            "MN": 1e6,
            "lb": .45359237,
            "kip": 4448.2216152605,
        }

    def giveDict(self):
        return self.unit_dict
