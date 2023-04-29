import importlib

from sympy import symbols, sympify, Eq
import sympy as sp
from math import floor, log10
from copy import deepcopy


def solve(info):
    inputs = info["input"]
    formula = info["formula"]
    solve_method = info["solve_method"]
    bonus_method = info["Bonus"]

    unitConvert(inputs, solve_method)
    output_dict = deepcopy(inputs)
    extra = bonus_method(info)

    if formula != "":
        sol = solveEquation(formula, inputs)
        list_to_5_sig_figs(sol)
    else:
        info["output"] = extra


    for i in inputs:
        if safe_float(inputs[i]["value"], ""):
            output_dict[i]["value"] = safe_float(inputs[i]["value"], "")
        else:
            try:
                output_dict[i]["value"] = sol
            except Exception:
                pass
    if formula != "":
        info["output"] = output_dict

    print(info)
    return info


def safe_float(value, special_type):
    try:
        result = float(value)
        return result
    except (ValueError, TypeError):
        result = None


def unitConvert(inputs, solve_method):
    for i, element in enumerate(inputs):
        mod_name = f"apex.Units.{inputs[element]['dimension']}"
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


        if not safe_float(inputs[element]["value"], "") is None and not solve_method == "beam":
            inputs[element]["value"] = unit_dict[inputs[element]["unit"]] * safe_float(inputs[element]["value"], "")


def solveEquation(formula, inputs):
    # Define symbols for variables based on the keys of the input_dict
    symbols_list = symbols(' '.join(inputs.keys()))

    ls, rs = formula.split("==")

    ls = sympify(ls)
    rs = sympify(rs)

    eqn = Eq(ls, rs)

    for i, element in enumerate(inputs):
        eqn = eqn.subs(symbols_list[i], inputs[element]["value"])

    sol = sp.solve(eqn)

    return sol


def list_to_5_sig_figs(sol):
    for i, element in enumerate(sol):
        sol[i] = round(float(element), -int(floor(log10(abs(element)))) + 4)

# solve(info)
