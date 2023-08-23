from pint import UnitRegistry
from apex.Helper import UnitHelper

import unittest

class TestUnitConversion(unittest.TestCase):

    def setUp(self):
        self.ureg = UnitRegistry()
        self.Q_ = self.ureg.Quantity

    def check_unit_conversion_factors(self, dimension):
        unit_dict = UnitHelper.get_unit_dict(dimension)

        with self.subTest(f"Test conversion factors for {dimension} units"):
            for unit_name, conversion_factor in unit_dict.items():
                try:
                    unit = self.ureg(unit_name)
                    self.assertAlmostEqual(unit.to_base_units().magnitude, conversion_factor, msg=f"\nDimension: {dimension}, Unit: {unit_name}")
                except Exception as e:
                    self.fail(f"Error defining unit '{unit_name}': {e} \nDimension: {dimension}, Unit: {unit_name}")

        return dimension, unit_dict

    def test_unit_conversions(self):

        results = []
        for dimension in UnitHelper.get_all_dimensions():

            result = self.check_unit_conversion_factors(dimension)
            results.append(result)
