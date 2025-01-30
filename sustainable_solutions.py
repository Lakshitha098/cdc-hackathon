from scipy.optimize import linprog

# Objective: Minimize CO2 emissions by adjusting energy usage in different sectors
# Coefficients of the objective function (emission factors for different energy sources)
c = [-0.5, -0.3, -0.2]  # Negative for minimization (reduce emissions)

# Constraints (e.g., maximum energy usage, sustainability goals)
A = [[1, 1, 0], [0, 1, 1]]  # Maximum energy limits
b = [500, 300]  # Limits in respective units

# Bounds for each energy source (e.g., minimum and maximum usage)
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)

# Solve the optimization problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='highs')

# Display the solution
print(f'Optimal energy mix: {res.x}')
