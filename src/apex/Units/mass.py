from apex.Helper.UnitFactory import UnitFactory

class mass(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "kg": 1,
            "g": .001,
            "Mg": 1000,
            "lb": .45359237,
            "kip": 4448.2216152605,
            "oz": 0.0283495,
            "metric_ton": 1000,
            "US_ton" : 907.18474,
            "ozt": 0.0311035,
        }

    def giveDict(self):
        return self.unit_dict
