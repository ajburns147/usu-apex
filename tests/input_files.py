import importlib
import os

import unittest


class TestInputFiles(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.apex_dir = "../src/apex/"
        self.all_input_files = []

        for root, dirs, files in os.walk(self.apex_dir):
            if root.count(os.sep) - self.apex_dir.count(os.sep) == 2:
                for file in files:
                    if "__" not in file:
                        path = os.path.join(root, file).replace(self.apex_dir, "").replace("\\", ".")[:-3]
                        self.all_input_files.append(path)

    def test_classes_named_correctly(self):
        for path in self.all_input_files:
            module_name = path.split('.')[-1]
            module = importlib.import_module(f"apex.{path}")
            my_obj = getattr(module, module_name)

            with self.subTest(module=module_name):
                self.assertIsNotNone(my_obj)

    def test_have_correct_dict(self):
        for path in self.all_input_files:
            module_name = path.split('.')[-1]
            module = importlib.import_module(f"apex.{path}")
            my_obj = getattr(module, module_name)()
            info = my_obj.giveInfo()

            with self.subTest(module=module_name):
                required_in_info = "input formula Note solve_method plot_method Bonus".split()
                for element in required_in_info:
                    self.assertIn(element, info.keys())
