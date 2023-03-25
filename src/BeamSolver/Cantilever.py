import numpy as np
import sympy

# Example input list with string numbers
output_dict = ["17 -38*np.cos(np.pi/4)", "-10 30 38*np.cos(np.pi/4)", "-10 90 (5*38*np.cos(np.pi/4))"]

variables_passed = []

for string in output_dict:
    split_string = string.split()
    new_sublist = []
    for substring in split_string:
        if '*' in substring:  # check if the substring contains multiplication
            new_sublist.append(eval(substring))  # evaluate the expression and append to the new sublist
        else:
            new_sublist.append(float(substring))  # convert the string to float and append to the new sublist
    variables_passed.append(new_sublist)

print(variables_passed)



x, y, m = sympy.symbols('x y m')

variables=[x,y,m]

for i in range(len(variables_passed)):
    variables_passed[i].extend([variables[i]])

print(variables_passed)

# Define the equations
eq1 = sympy.Eq(sum(variables_passed[0]), 0)
eq2 = sympy.Eq(sum(variables_passed[1]), 0)
eq3 = sympy.Eq(sum(variables_passed[2]), 0)

# Solve the system of equations
sol = sympy.solve((eq1, eq2, eq3), (x, y, m))

# Print the solution
print(sol)