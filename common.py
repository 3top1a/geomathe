import math
import sympy as sp
import inspect

# Data input
def data_input(data):
    for name in data:
        while True:
            try:
                value = input(f"Enter {name}: ")
                if value == "":
                    break
                if float(value) > 0:
                    data[name] = float(value)
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

def solve_equation_auto(data, equations):
    for eq_name, equation in equations.items():
        variables = {name: sp.symbols(name) for name in data.keys()}
        
        solve_for = None
        for name, value in data.items():
            if value is None and name in equation['vars']:
                solve_for = name
                break
        if solve_for is None:
            continue
        
        substitutions = {variables[name]: value for name, value in data.items() if value is not None and name in equation['vars']}
        sympy_equation = equation['eq'](**variables)
        solution = sp.solve(sympy_equation, variables[solve_for])
        data[solve_for] = solution[0].subs(substitutions).evalf()

def generate_equations_dict(*calc_functions):
    equations = {}
    for func in calc_functions:
        func_name = func.__name__
        params = inspect.signature(func).parameters
        equations[func_name] = {
            'eq': func,
            'vars': list(params.keys())
        }
    return equations

def print_data(data):
    print("---")
    print()
    for (k, v) in data.items():
        print(f"{k}: {v}")

def calc(variables, equations):
    data_input(variables)
    equations = generate_equations_dict(*equations)
    solve_equation_auto(variables, equations)
    print_data(variables)
