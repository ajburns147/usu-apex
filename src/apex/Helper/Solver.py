import importlib

from sympy import symbols, sympify, Eq
import sympy as sp
from math import floor, log10
from copy import deepcopy


def solve(info):
    """
    Solves an equation and/or performs unit conversion on the input dictionary.

        Args:
            info (dict): The master info dict object.

        Returns:
            dict: A completed form of the input object, which includes the computed output.
    """

    inputs = info["input"]
    formula = info["formula"]
    solve_method = info["solve_method"]
    bonus_method = info["Bonus"]

    for variable in inputs:
        if "value" not in inputs[variable]:
            inputs[variable]["value"] = ""

    unitConvert(inputs, solve_method)
    output_dict = deepcopy(inputs)
    extra = bonus_method(info)

    if formula is not None:
        soln = solveEquation(formula, inputs)
        list_to_5_sig_figs(soln)
    else:
        info["output"] = extra

    for variable in inputs:
        if "value" not in inputs[variable]:
            inputs[variable]["value"] = ""

        if safe_float(inputs[variable]["value"]):
            output_dict[variable]["value"] = safe_float(inputs[variable]["value"])
        else:
            try:
                output_dict[variable]["value"] = soln
            except Exception:
                pass
    if formula is not None:
        info["output"] = output_dict

    # print(info)
    return info


def safe_float(value):
    """
    Converts a value to a float if possible.

        Args:
            value (str): The value to convert.

        Returns:
            float or None: The float value or None, indicating the operation failed.
    """
    try:
        if value == "":
            return None
        result = float(value)
        return result
    except (ValueError, TypeError):
        return None


def unitConvert(inputs, solve_method):
    """
    Converts the input values to their specified unit in the input dict.

        Args:
            inputs (dict): A dictionary containing the input values, which are a subdict of the mater info object.
            solve_method (str): The method used to solve the equation.
    """
    for i, variable in enumerate(inputs):
        mod_name = f"apex.Units.{inputs[variable]['dimension']}"
        module = importlib.import_module(mod_name)

        class_obj = None
        class_count = 0
        for name, obj in module.__dict__.items():
            if isinstance(obj, type):
                class_count += 1
                if class_count == 2:
                    class_obj = obj
                    break

        my_obj = class_obj()

        unit_dict = my_obj.giveDict()

        if safe_float(inputs[variable]["value"]) and solve_method != "beam":
            inputs[variable]["value"] = unit_dict[inputs[variable]["unit"]] * safe_float(inputs[variable]["value"])


def solveEquation(formula, inputs):
    """
    Solves an equation by substituting inputs into the provided formula and solving.

        Args:
            formula (str): The equation to solve.
            inputs (dict): A dictionary containing the input values.

        Returns:
            list: The solutions of the equation.
    """
    # Define symbols for variables based on the keys of the input_dict
    symbols_list = symbols(' '.join(inputs.keys()))

    ls, rs = formula.split("==")

    ls = sympify(ls)
    rs = sympify(rs)

    eqn = Eq(ls, rs)

    for i, variable in enumerate(inputs):
        try:
            eqn = eqn.subs(symbols_list[i], inputs[variable]["value"])
        except TypeError:
            continue
    sol = sp.solve(eqn)

    return sol


def list_to_5_sig_figs(soln):
    """
    Takes a list and rounds the solutions to 5 significant figures.

        Args:
            soln (list): The solutions of the equation.

        Returns:
            N/A: mutates the provided list
    """
    for i, element in enumerate(soln):
        if type(element) in [dict, complex]:
            continue

        if element == 0:
            continue

        # print(f"{element}=    {type(element)=}")

        try:
            soln[i] = round(element, -int(floor(log10(abs(element)))) + 4)
        except TypeError:
            continue
