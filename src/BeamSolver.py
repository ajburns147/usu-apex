import sympy
import numpy as np

import sympy
variables_passed = [[17, -38*np.cos(np.pi/4)],[-10, 30, 38*np.cos(np.pi/4)], [-10, 90, (5*38*np.cos(np.pi/4))]]

x, y, z = sympy.symbols('x y z')

variables=[x,y,z]

for i in range(len(variables_passed)):
    variables_passed[i].extend([variables[i]])

print(variables_passed)

# Define the equations
eq1 = sympy.Eq(sum(variables_passed[0]), 0)
eq2 = sympy.Eq(sum(variables_passed[1]), 0)
eq3 = sympy.Eq(sum(variables_passed[2]), 0)

# Solve the system of equations
sol = sympy.solve((eq1, eq2, eq3), (x, y, z))

# Print the solution
print(sol)