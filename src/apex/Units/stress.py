from apex.Helper.UnitFactory import UnitFactory

class stress(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "Pa": 1,
            "kPa": 1000,
            "psi": 6894.7572931683635,
        }

    def giveDict(self):
        return self.unit_dict
