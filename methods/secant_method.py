import numpy as np

title = 'Січних'

def secant_method(func, initial_guess, tolerance, max_iterations):
    f = lambda x: eval(func, {"x": x, "np": np})

    x0 = initial_guess
    x1 = x0 + 0.1
    for i in range(max_iterations):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1) < tolerance:
            return x1, i

        if x1 == x0:
            raise ValueError("Ділення на нуль. Неможливо продовжити ітерації.")

        x_temp = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x_temp
    
    raise ValueError("Досягнуто максимальну кількість ітерацій без знаходження кореня.")
