import math
import sympy as sp
import inspect

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

def solve_equation_auto(data, equations, max_iterations=10):
    solved_in_this_iteration = True
    iteration = 0

    while solved_in_this_iteration and iteration < max_iterations:
        solved_in_this_iteration = False
        iteration += 1

        for eq_name, equation in equations.items():
            variables = {name: sp.symbols(name) for name in data.keys()}
            solve_for = None

            for name in equation['vars']:
                if name in data and data[name] is None:
                    solve_for = name
                    break

            if solve_for is None:
                continue

            substitutions = {variables[name]: value for name, value in data.items() if value is not None and name in equation['vars']}
            sympy_equation = equation['eq'](**variables)

            try:
                solution = sp.solve(sympy_equation, variables[solve_for])
                print(f"{solve_for} =", sp.latex(solution).replace("\\left[", "").replace("\\right]", "").strip())
                if solution:
                    numerical_solution = solution[0].subs(substitutions).evalf()
                    if numerical_solution.is_Number:
                        print(f"{solve_for} = {numerical_solution}")
                        print()
                        data[solve_for] = numerical_solution
                        solved_in_this_iteration = True
            except Exception as e:
                print(f"Could not solve for {solve_for}: {e}")

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
    print()
    equations = generate_equations_dict(*equations)
    solve_equation_auto(variables, equations)
    print_data(variables)
