import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import re
from newton_solver import NewtonSolver

class NewtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Метод Ньютона для нелінійних рівнянь')
        
        # Labels and input fields
        self.function_label = QLabel('Введіть рівняння f(x):', self)
        self.function_input = QLineEdit(self)
        
        self.initial_label = QLabel('Введіть початкове наближення:', self)
        self.initial_input = QLineEdit(self)
        
        self.tolerance_label = QLabel('Введіть точність (за замовчуванням 1e-6):', self)
        self.tolerance_input = QLineEdit(self)
        
        self.iterations_label = QLabel('Максимальна кількість ітерацій (за замовчуванням 100):', self)
        self.iterations_input = QLineEdit(self)
        
        # Button to solve
        self.solve_button = QPushButton('Розв\'язати', self)
        self.solve_button.clicked.connect(self.solve_equation)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.initial_label)
        layout.addWidget(self.initial_input)
        layout.addWidget(self.tolerance_label)
        layout.addWidget(self.tolerance_input)
        layout.addWidget(self.iterations_label)
        layout.addWidget(self.iterations_input)
        layout.addWidget(self.solve_button)
        
        self.setLayout(layout)
        
    def solve_equation(self):
        function = self.function_input.text().strip()
        initial_guess_text = self.initial_input.text().strip()
        tolerance_text = self.tolerance_input.text().strip()
        iterations_text = self.iterations_input.text().strip()

        # Перевірка на некоректні символи (не математика або не англійські букви)
        if re.search(r"[А-Яа-я]", function):
            QMessageBox.warning(self, "Помилка", "Рівняння не повинно містити кириличні символи!")
            return

        # Перевірка введення початкового наближення
        try:
            initial_guess = float(initial_guess_text)
        except ValueError:
            QMessageBox.warning(self, "Помилка", "Будь ласка, введіть коректне початкове наближення (число)!")
            return

        # Перевірка введення точності
        if tolerance_text:
            try:
                tolerance = float(tolerance_text)
                if tolerance <= 0:
                    raise ValueError
            except ValueError:
                QMessageBox.warning(self, "Помилка", "Точність повинна бути додатнім числом!")
                return
        else:
            tolerance = 1e-6  # Значення за замовчуванням

        # Перевірка введення кількості ітерацій
        if iterations_text:
            try:
                max_iterations = int(iterations_text)
                if max_iterations <= 0:
                    raise ValueError
            except ValueError:
                QMessageBox.warning(self, "Помилка", "Кількість ітерацій повинна бути додатнім цілим числом!")
                return
        else:
            max_iterations = 100  # Значення за замовчуванням

        # Спроба обчислення за допомогою методу Ньютона
        try:
            # Створення екземпляра класу вирішення (NewtonSolver) тут.
            solver = NewtonSolver(function, initial_guess, tolerance, max_iterations)
            root, iterations = solver.solve()
            QMessageBox.information(self, "Результат", f"Корінь: {root}\nКількість ітерацій: {iterations}")
        except Exception as e:
            QMessageBox.warning(self, "Помилка", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NewtonApp()
    ex.show()
    sys.exit(app.exec_())
