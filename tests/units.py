import importlib
import os
from pint import UnitRegistry

import unittest

apex_dir = "../src/apex/"

unit_file_list = os.listdir(apex_dir + "Units")


class TestUnitConversion(unittest.TestCase):

    def setUp(self):
        self.ureg = UnitRegistry()
        self.Q_ = self.ureg.Quantity
        # self.ureg.set_base_units('kilonewton')

    def check_unit_conversion_factors(self, module_name):
        module = importlib.import_module(f"apex.Units.{module_name}")
        my_obj = getattr(module, module_name)()
        unit_dict = my_obj.giveDict()

        with self.subTest(f"Test conversion factors for {module_name} units"):
            for unit_name, conversion_factor in unit_dict.items():
                try:

                    unit = self.ureg(unit_name)
                    self.assertAlmostEqual(unit.to_base_units().magnitude, conversion_factor, msg=f"\nFile: {module_name}, Unit: {unit_name}")
                except Exception as e:
                    self.fail(f"Error defining unit '{unit_name}': {e} \nFile: {module_name}, Unit: {unit_name}")

        return module_name, unit_dict

    def test_unit_conversions(self):

        results = []
        for unit_file in unit_file_list:
            if unit_file[-3:] != ".py" or "_" in unit_file:
                continue

            module_name = unit_file[:-3]
            result = self.check_unit_conversion_factors(module_name)
            results.append(result)
