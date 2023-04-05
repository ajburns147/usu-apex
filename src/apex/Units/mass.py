from src.apex.Helper.UnitFactory import UnitFactory

class mass(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "kg": 1,
            "g": 1000,
            "Mg": .001,
            "lb": 2.2046,
            "kip": 2.2046 * 10**-3,
            "oz": 0.0283495,
            "metric ton": 1000,
            "US ton" : 907.185,
            "ozt": 0.0311035,
        }

    def giveDict(self):
        return self.unit_dict
