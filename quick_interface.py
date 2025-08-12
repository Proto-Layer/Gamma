# quick_interface.py
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
import random

class QuickInterface:
    def __init__(self):
        self.app = QApplication([])
        self.control = QMainWindow()
        self.display = QMainWindow()
        self.label = QLabel("Hello, Quick World!")

        self.setup_control()
        self.setup_display()

    def setup_control(self):
        self.control.setWindowTitle("Quick Control")
        container = QWidget()
        layout = QVBoxLayout(container)

        change_color_btn = QPushButton("Randomize Text Color")
        change_color_btn.clicked.connect(self.randomize_text_color)
        layout.addWidget(change_color_btn)

        quit_btn = QPushButton("Quit")
        quit_btn.clicked.connect(self.app.quit)
        layout.addWidget(quit_btn)

        self.control.setCentralWidget(container)
        self.control.resize(300, 200)
        self.control.show()

    def setup_display(self):
        font = QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(self.label)

        self.display.setWindowTitle("Quick Display")
        self.display.setCentralWidget(container)
        self.display.showFullScreen()

    def randomize_text_color(self):
        r, g, b = [random.randint(0, 255) for _ in range(3)]
        self.label.setStyleSheet(f"color: rgb({r},{g},{b});")

    def start(self):
        self.app.exec()

if __name__ == "__main__":
    qi = QuickInterface()
    qi.start()
