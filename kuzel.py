import sympy as sp
from common import calc
import math

vars = {
    "r": None,
    "s": None,
    "v": None,
    "V": None,
    "S": None,
    "Sp": None,
    "Spl": None,
}

# "s² = r² + v²"
def calculate_slant_height(r, s, v, **kwargs):
    return sp.sqrt(v**2 + r**2) - s

# "V = ⅓ πr²v"
def calculate_volume(r, v, V, **kwargs):
    return (1/3) * sp.pi * r**2 * v - V

# "S = πr ⋅ (r + s)"
def calculate_surface_area(r, s, S, **kwargs):
    return sp.pi * r * (r + s) - S

# "S = Sₚ + Sₚₗ"
def calculate_surface_area2(Sp, Spl, S, **kwargs):
    return Sp + Spl - S

# "Sₚ = πr²"
def calculate_bottom_surface_area(r, Sp, **kwargs):
    return sp.pi * r**2 - Sp

# "Sₚₗ = πrs"
def calculate_lateral_surface_area(r, s, Spl, **kwargs):
    return sp.pi * r * s - Spl

equations = [
    calculate_slant_height, 
    calculate_volume,
    calculate_bottom_surface_area,
    calculate_lateral_surface_area,
    calculate_surface_area2,
    calculate_surface_area,
]

calc(vars, equations)
