from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel("Something will happen soon...probably")
label.show()

app.exec()
