import sympy as sp
from sympy import symbols, sympify, Eq
from copy import deepcopy

from apex.Helper import UnitHelper

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

    # Ensure all variables have a "value" key in the inputs dictionary
    for variable in inputs:
        if "value" not in inputs[variable]:
            inputs[variable]["value"] = ""

    # Perform unit conversion based on the specified unit for each variable
    unit_convert(inputs, solve_method)

    # Create a deep copy of the inputs to store the output values
    output_dict = deepcopy(inputs)

    # Execute the bonus_method if a formula is not provided
    if formula is None:
        info["output"] = bonus_method(info)
    else:
        # Solve the equation using the provided formula
        sol = solve_equation(formula, inputs)

        # Update the output_dict with the computed solutions
        for variable in inputs:
            if safe_float(inputs[variable]["value"]):
                output_dict[variable]["value"] = safe_float(inputs[variable]["value"])
            else:
                try:
                    output_dict[variable]["value"] = sol
                except Exception:
                    pass

        info["output"] = output_dict

    # Return the updated info dictionary
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


def unit_convert(inputs, solve_method):
    """
    Converts the input values to their specified unit in the input dict.

    Args:
        inputs (dict): A dictionary containing the input values, which are a subdict of the master info object.
        solve_method (str): The method used to solve the equation.
    """
    for i, variable in enumerate(inputs):
        dimension = inputs[variable]['dimension']

        unit_dict = UnitHelper.get_unit_dict(dimension)

        if safe_float(inputs[variable]["value"]) and solve_method != "beam":
            inputs[variable]["value"] = unit_dict[inputs[variable]["unit"]] * safe_float(inputs[variable]["value"])


def solve_equation(formula, inputs):
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

    # Ensure the solution is in 5 sig figs
    try:  # if list
        rounded_sol = [sp.N(s, 5) for s in sol]
    except AttributeError:    # if dict
        rounded_sol = [{key: sp.N(value, 5)} for solution in sol for key, value in solution.items()]

    return rounded_sol
