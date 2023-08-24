import sympy as sp
from sympy import symbols, sympify, Eq
from copy import deepcopy

from apex.Helper import UnitHelper

def solve(info):
    print(info)
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
    input_unit_convert(inputs)

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

        output_unit_convert(output_dict)

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


def input_unit_convert(inputs):
    """
    Converts the input values to their specified unit in the input dict.

    Args:
        inputs (dict): A dictionary containing the input values, which are a subdict of the master info object.
    """
    for variable in inputs:
        dimension = inputs[variable]['dimension']
        from_unit = inputs[variable]['wanted_unit']
        to_unit = UnitHelper.get_base_unit(dimension)

        value = inputs[variable]['value']
        value = safe_float(value)

        if not value:
           pass
        elif isinstance(value, float) or isinstance(value, int):
            value = float(value)
            inputs[variable]["value"] = UnitHelper.convert(dimension, value, from_unit, to_unit)
        elif isinstance(value, list):
            value = [UnitHelper.convert(dimension, float(val), from_unit, to_unit) for val in value]
            inputs[variable]["value"] = value
        else:
            raise RuntimeError(f"Bad conversion for {value} ({type(value)})")

        inputs[variable]["curr_unit"] = UnitHelper.get_base_unit(dimension)


def output_unit_convert(outputs):
    """
    Converts the input values to their specified unit in the input dict.

    Args:
        outputs (dict): A dictionary containing the input values, which are a subdict of the master info object.
    """
    for variable in outputs:
        dimension = outputs[variable]['dimension']
        from_unit = UnitHelper.get_base_unit(dimension)
        to_unit = outputs[variable]['wanted_unit']

        value = outputs[variable]['value']
        value = safe_float(value)

        if not value:
            pass
        elif isinstance(value, float) or isinstance(value, int):
            value = float(value)
            outputs[variable]["value"] = UnitHelper.convert(dimension, value, from_unit, to_unit)
        elif isinstance(value, list):
            value = [UnitHelper.convert(dimension, float(val), from_unit, to_unit) for val in value]
            outputs[variable]["value"] = value
        else:
            raise RuntimeError(f"Bad conversion for {value}")

        outputs[variable]["curr_unit"] = outputs[variable]["wanted_unit"]

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


if __name__ == "__main__":
    a_val = "3"
    b_val = "4"
    c_val = ""

    info = {
               'input': {
                   'a': {
                       'default_value': 3, 'dimension': 'length', 'value': a_val, 'wanted_unit': 'm'
                   },
                   'b': {
                       'default_value': 4, 'dimension': 'length', 'value': b_val, 'wanted_unit': 'km'
                   },
                   'c': {
                       'default_value': None, 'dimension': 'length', 'value': c_val, 'wanted_unit': 'km'}
               },
               'formula': 'a**2 + b**2 == c**2',
               'Note': "This is Pythagoras's theorem",
               'solve_method': '',
               'plot_method': False,
               'Bonus': None
    }

    output = solve(info)['output']
    for i in output:
        print(f"{i} : {output[i]}")
