import unittest
from methods.newton_method import newton_method

class TestNewtonMethod(unittest.TestCase):
    def test_simple_equation(self):
        # Тест простого рівняння: x^2 - 4 = 0, корінь якого 2 або -2
        func = "x**2 - 4"
        initial_guess = 1.0
        tolerance = 1e-6
        max_iterations = 100

        root, iterations = newton_method(func, initial_guess, tolerance, max_iterations)
        self.assertAlmostEqual(root, 2.0, places=5)

    def test_high_tolerance(self):
        # Тест для рівняння x - 1 = 0 з високою точністю
        func = "x - 1"
        initial_guess = 0.5
        tolerance = 1e-10
        max_iterations = 100

        root, iterations = newton_method(func, initial_guess, tolerance, max_iterations)
        self.assertAlmostEqual(root, 1.0, places=9)


if __name__ == "__main__":
    unittest.main()
