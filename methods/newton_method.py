import numpy as np


title = 'Ньютона'

def newton_method(func, initial_guess, tolerance, max_iterations):
    f = lambda x: eval(func, {"x": x, "np": np})
    df = lambda x: (f(x + 1e-6) - f(x)) / 1e-6

    x_n = initial_guess
    for i in range(max_iterations):
        f_value = f(x_n)
        f_prime_value = df(x_n)

        if abs(f_value) < tolerance:
            return x_n, i

        if f_prime_value == 0:
            raise ValueError("Похідна дорівнює нулю. Неможливо продовжити ітерації.")

        x_n = x_n - f_value / f_prime_value
    
    raise ValueError("Досягнуто максимальну кількість ітерацій без знаходження кореня.")
