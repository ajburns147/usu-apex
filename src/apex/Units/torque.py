from apex.Helper.UnitFactory import UnitFactory

class torque(UnitFactory):
    def __init__(self):
        self.unit_dict = {
            "N*m": 1,
            "ft*lb": 0.138254954376,
            "in*lb": 0.011521246198,
            "mN*m": 0.001,
            "gf*cm": 9.80665e-05,
        }

    def giveDict(self):
        return self.unit_dict
