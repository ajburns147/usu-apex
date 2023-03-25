from sympy import symbols, sympify, Eq
import sympy as sp
from math import floor, log10
from copy import deepcopy

def solve(info):
    inputs = info["input"]
    formula = info["formula"]
    solve_method = info["solve_method"]
    bonus_method = info["Bonus"]

    if solve_method != "":
        bonus_method(info)

    # Define symbols for variables based on the keys of the input_dict
    symbols_list = symbols(' '.join(input_dict.keys()))

    ls, rs = formula.split("==")

    ls = sympify(ls)
    rs = sympify(rs)

    eqn = Eq(ls, rs)


    for i, element in enumerate(inputs):
        # print(f"Units.{inputs[element][2]}")
        module = __import__(f"Units.{inputs[element][2]}", fromlist=['*'])

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

        print(f"{unit_dict[inputs[element][3]]=}")
        print(f"{inputs[element]=}")

        if not safe_float(inputs[element][0], "") is None:
            inputs[element][0] = unit_dict[inputs[element][3]] * safe_float(inputs[element][0], "")

    for i, element in enumerate(inputs):
        eqn = eqn.subs(symbols_list[i], inputs[element][0])

    sol = sp.solve(eqn)

    for i, element in enumerate(sol):
        sol[i] = round(float(element), -int(floor(log10(abs(element)))) + 4)

    print(f"{sol=}")

    output_dict = deepcopy(input_dict)

    for i in input_dict:
        if safe_float(inputs[i][0], ""):
            output_dict[i] = safe_float(inputs[i][0], "")
        else:
            output_dict[i] = sol

    info["output"] = output_dict

    print(info)



def Bonus(a):
    pass

input_dict = {
            "a": ["3", 3, "length", "km", ""],
            "b": ["4", 4, "length", "m", ""],
            "c": ["", 5, "length", "m", ""],
            }

info = {
     "input": input_dict,
     "formula": "a**2 + b**2 == c**2",
     "Note": "This is Pythagoras's theorem",
     "solve_method": "",
     "plot_method": False,
     "Bonus": Bonus("")
}

def safe_float(value, special_type):
    try:
        result = float(value)
        return result
    except (ValueError, TypeError):
        result = None



solve(info)
