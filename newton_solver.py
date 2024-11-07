import numpy as np

class NewtonSolver:
    def __init__(self, function_str, initial_guess, tolerance=1e-6, max_iterations=100):
        self.function_str = function_str
        self.initial_guess = initial_guess
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.function = self._parse_function(function_str)  # Перетворення функції з рядка
        
    def _parse_function(self, function_str):
        # Створюємо анонімну функцію з рядка (наприклад, 'np.sin(x) + x**2' -> lambda x: np.sin(x) + x**2)
        def func(x):
            return eval(function_str, {"np": np, "x": x})
        return func
        
    def _numerical_derivative(self, func, x, h=1e-5):
        # Обчислення похідної за допомогою методу кінцевих різниць
        return (func(x + h) - func(x - h)) / (2 * h)
    
    def solve(self):
        x_n = self.initial_guess
        for i in range(self.max_iterations):
            f_value = self.function(x_n)  # Значення функції в x_n
            f_prime_value = self._numerical_derivative(self.function, x_n)  # Числова похідна
            
            if abs(f_value) < self.tolerance:
                return x_n, i  # Повертаємо корінь і кількість ітерацій
            
            if f_prime_value == 0:
                raise ValueError("Похідна дорівнює нулю. Неможливо продовжити ітерації.")
            
            x_n = x_n - f_value / f_prime_value  # Метод Ньютона
        
        raise ValueError("Досягнуто максимальну кількість ітерацій без знаходження кореня.")