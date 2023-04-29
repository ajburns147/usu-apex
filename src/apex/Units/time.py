from apex.Helper.UnitFactory import UnitFactory

class time(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "sec": 1,
            "min": 60,
            "hour": 60*60,
            "day": 60*60*24,
            "week": 60*60*24*7,
            "year": 31557600,
            "ms": .001,
            "μs": 10**-6,
            "ns": 10**-9,
        }

    def giveDict(self):
        return self.unit_dict
