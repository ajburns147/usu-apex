from sympy import symbols, sympify, lambdify


def solve(info):
    inputs = info["input"]
    formula = info["formula"]
    solve_method = info["solve_method"]
    bonus_method = info["bonus"]

    if solve_method != "":
        bonus_method(info)

    # Get a list of variable names from the keys of the dictionary
    var_names = list(inputs.keys())

    # Use SymPy's symbols() function to create a list of SymPy symbols from the variable names
    sym_vars = symbols(var_names)

    # Create a dictionary that maps each variable name to its corresponding symbol
    sym_dict = dict(zip(var_names, sym_vars))

    # Replace the variables in the original dictionary with their corresponding symbols
    for var_name, var_list in inputs.items():
        inputs[var_name] = [sym_dict[var_name][i] for i in range(len(var_list))]

    # Print the updated dictionary
    print(inputs)


    # Use SymPy's sympify() function to convert the formula string to a SymPy expression
    formula_expr = sympify(formula)

    # Define a dictionary that maps each symbol to its corresponding list of values
    sym_dict = dict(zip(sym_vars, [inputs[var_name] for var_name in var_names]))

    # Use SymPy's lambdify() function to create a function that can evaluate the formula for any set of variable values
    eval_formula = lambdify(sym_vars, formula_expr)

    # Evaluate the formula for the values in the first row of the variable lists
    result = eval_formula(*[sym_dict[sym][0] for sym in sym_vars])

    # Add the results to "output"

def custom_solve():
