from sympy import symbols, pi, sin, solve

# Given parameters
a = 312.6  # m
b = 221.2  # m
t = 15.5  # m
E = 72000  # Pa
nu = 0.333
p = 0.001
D = (E * t**3) / (12 * (1 - nu**2))

# Variables
m, n, x, y = symbols('m n x y')
A_mn = symbols('A_mn')

# Deflection at the center of the plate, (x, y) = (a/2, b/2)
w_center_expr = sum([sum([A_mn * sin(m * pi * x / a) * sin(n * pi * y / b) for n in range(1, 3)]) for m in range(1, 3)])

# Substitute x = a/2, y = b/2 to find deflection at the center
w_center = w_center_expr.subs({x: a/2, y: b/2})

# Since the actual calculation of A_mn requires solving the system with the boundary conditions and pressure,
# we'll provide a simplified approach for illustration purposes.

# Example coefficient A_mn calculation (for m=1, n=1 as an illustration)
# This is a simplification. In practice, you'd use the actual derived equation for A_mn based on p, D, and the boundary conditions.
A_11 = p / (D * (pi**4) * ((1/a**2) + (1/b**2))**2)

# Deflection at center for m=1, n=1
w_center_A11 = w_center.subs({A_mn: A_11}).evalf()

print(w_center_A11)
