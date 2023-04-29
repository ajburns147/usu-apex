from apex.Helper.UnitFactory import UnitFactory

class pressure(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "Pa": 1,
            "kPa": 1000,
            "psi": 6894.7572931683635,
            "bar": 1e5,
            "atm": 101325,
            "mmHg": 133.322387415,
        }

    def giveDict(self):
        return self.unit_dict
