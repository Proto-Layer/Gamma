# extras.py
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QFont
import random

class RandomColorWidget(QWidget):
    """A small widget that displays a label and changes its text color randomly."""
    def __init__(self):
        super().__init__()
        self.label = QLabel("Random Color Label")
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)

        self.button = QPushButton("Change Color")
        self.button.clicked.connect(self.change_color)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def change_color(self):
        r, g, b = [random.randint(0, 255) for _ in range(3)]
        self.label.setStyleSheet(f"color: rgb({r},{g},{b});")
