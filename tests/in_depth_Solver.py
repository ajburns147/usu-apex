from apex.Helper import Solver
from apex.Input_Files.Math.Trigonometry.Pythagorean_Theorem import Pythagorean_Theorem
from copy import deepcopy

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

    def test_solver_fuzzer(self):
        Solver.solve(self.info)

        info = deepcopy(self.info)

        for a in self.example_input:
            for b in self.example_input:
                for c in self.example_input:
                    info["input"]["a"]["value"] = a
                    info["input"]["b"]["value"] = b
                    info["input"]["c"]["value"] = c

                    with self.subTest(f"Fuzz testing for {a=} {b=} {c=}"):
                        Solver.solve(info)
