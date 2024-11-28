import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox
import os
import importlib


class SolverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.methods = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рішення нелінійних рівнянь')

        # Створення основного макета
        self.layout = QVBoxLayout(self)
        
        # Заголовки і поля вводу
        self.function_label = QLabel('Введіть рівняння f(x):', self)
        self.layout.addWidget(self.function_label)
        
        self.function_input = QLineEdit(self)
        self.layout.addWidget(self.function_input)
        
        self.initial_label = QLabel('Введіть початкове наближення:', self)
        self.layout.addWidget(self.initial_label)
        
        self.initial_input = QLineEdit(self)
        self.layout.addWidget(self.initial_input)
        
        self.tolerance_label = QLabel('Введіть точність (за замовчуванням 1e-6):', self)
        self.layout.addWidget(self.tolerance_label)
        
        self.tolerance_input = QLineEdit(self)
        self.layout.addWidget(self.tolerance_input)
        
        self.iterations_label = QLabel('Максимальна кількість ітерацій (за замовчуванням 100):', self)
        self.layout.addWidget(self.iterations_label)
        
        self.iterations_input = QLineEdit(self)
        self.layout.addWidget(self.iterations_input)
        
        # Завантаження методів
        self.load_methods()

        # Якщо методів більше одного, відображаємо випадаючий список
        if len(self.methods) > 1:
            self.method_label = QLabel('Виберіть метод:', self)
            self.layout.addWidget(self.method_label)
            
            self.method_combo = QComboBox(self)
            self.method_combo.addItems(self.methods.keys())  # Додаємо назви методів у випадаючий список
            self.layout.addWidget(self.method_combo)

        # Кнопка для розв'язку
        self.solve_button = QPushButton('Розв\'язати', self)
        self.solve_button.clicked.connect(self.solve_equation)
        self.layout.addWidget(self.solve_button)
        
        self.setLayout(self.layout)  # Встановлюємо основний макет для віджета

    def load_methods(self):
        """ Динамічно завантажує методи з папки 'methods'. """
        methods_path = os.path.join(os.path.dirname(__file__), 'methods')
        
        for filename in os.listdir(methods_path):
            if filename.endswith(".py"):
                method_name = filename[:-3]  # Видаляємо ".py"
                module_path = f"methods.{method_name}"  # Формуємо шлях до модуля
                module = importlib.import_module(module_path)  # Імпортуємо модуль

                if hasattr(module, method_name) and hasattr(module, 'title'):
                    self.methods[module.title] = getattr(module, method_name)

    def solve_equation(self):
        function = self.function_input.text().strip()
        initial_guess_text = self.initial_input.text().strip()
        tolerance_text = self.tolerance_input.text().strip()
        iterations_text = self.iterations_input.text().strip()

        # Перевірка введених даних
        try:
            initial_guess = float(initial_guess_text)
        except ValueError:
            QMessageBox.warning(self, "Помилка", "Будь ласка, введіть коректне початкове наближення (число)!")
            return

        if tolerance_text:
            try:
                tolerance = float(tolerance_text)
            except ValueError:
                QMessageBox.warning(self, "Помилка", "Точність повинна бути числом!")
                return
        else:
            tolerance = 1e-6

        if iterations_text:
            try:
                max_iterations = int(iterations_text)
            except ValueError:
                QMessageBox.warning(self, "Помилка", "Кількість ітерацій повинна бути числом!")
                return
        else:
            max_iterations = 100

        try:
            # Якщо методів більше одного, беремо вибраний з випадаючого списку
            if len(self.methods) > 1:
                selected_method_title = self.method_combo.currentText()
                selected_method = self.methods[selected_method_title]
            else:
                # Якщо метод тільки один, беремо його без вибору
                selected_method = list(self.methods.values())[0]

            # Виклик обраного методу
            root, iterations = selected_method(function, initial_guess, tolerance, max_iterations)
            QMessageBox.information(self, "Результат", f"Корінь: {root}\nКількість ітерацій: {iterations}")

        except Exception as e:
            QMessageBox.warning(self, "Помилка", str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SolverApp()
    ex.show()
    sys.exit(app.exec_())
