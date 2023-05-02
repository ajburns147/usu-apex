import os

import unittest


class TestInitFiles(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.input_dir = "../src/apex/Input_Files"

    def test_check_init_files(self):
        for root, dirs, files in os.walk(self.input_dir):

            # skip __pycache__ folder
            if os.path.basename(root) == "__pycache__":
                continue

            with self.subTest(directory=root):
                self.assertIn("__init__.py", files, f"{root=} missing __init__.py file")
