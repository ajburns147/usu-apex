from apex.Helper import Solver
from apex.Input_Files.Math.Trigonometry.Pythagorean_Theorem import Pythagorean_Theorem

import unittest


class TestSolver(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.info = Pythagorean_Theorem().giveInfo()
        self.formula = self.info["formula"]

        self.example_input = [
            "",
            # "-1",
            "a",
            "0.0",
            "2 + 1j",
            "sin()",
            "sin(4)",
        ]

    def test_no_runtime_errors(self):
        Solver.solve(self.info)

        for a in self.example_input:
            for b in self.example_input:
                for c in self.example_input:
                    self.info["input"]["a"]["value"] = a
                    self.info["input"]["b"]["value"] = b
                    self.info["input"]["c"]["value"] = c

                    with self.subTest(f"Fuzz testing for {a=} {b=} {c=}"):
                        Solver.solve(self.info)
