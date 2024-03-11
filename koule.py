import sympy as sp
from common import calc
import math

vars = {
    "r": None,
    "V": None,
    "S": None,
}

# "V = ⁴⁄₃πr³"
def calculate_volume(r, V, **kwargs):
    return (4/3) * sp.pi * r**3 - V

# "S = 4πr²"
def calculate_surface_area(r, S, **kwargs):
    return 4 * sp.pi * r**2 - S

# "r = (3V / (4π))**(1/3)"
def calculate_radius(V, r, **kwargs):
    return (3 * V / (4 * sp.pi))**(1/3) - r

equations = [
    calculate_volume,
    calculate_surface_area,
    calculate_radius,
]

calc(vars, equations)
