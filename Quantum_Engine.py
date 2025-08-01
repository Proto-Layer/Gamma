from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QLabel,
    QVBoxLayout, QWidget, QPushButton, QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class InterfaceManager:
    def __init__(self):
        self.app_instance = QApplication([])
        self.control_window = QMainWindow()
        self.display_window = QMainWindow()
        self.enable_dark_theme()

        self.initialize_control_ui()
        self.load_dashboard_view()

    def terminate_application(self):
        self.app_instance.quit()

    def generate_screen_info_label(self, screen):
        screen_size = screen.size()
        dpi = screen.physicalDotsPerInch()
        hz = screen.refreshRate()
        adjusted_font_size = dpi / 4

        font = QFont()
        font.setPointSizeF(adjusted_font_size)

        info_label = QLabel(
            f"Dimensions: {screen_size.width()}x{screen_size.height()}, DPI: {dpi}, Refresh Rate: {hz} Hz"
        )
        info_label.setFont(font)
        return info_label

    def retrieve_content_layout(self):
        container = self.display_window.centralWidget()
        layout = container.layout()
        for index in range(layout.count()):
            item = layout.itemAt(index)
            if isinstance(item.widget(), QScrollArea):
                return item.widget().widget().layout()
        return layout

    def insert_text_area(self):
        input_field = QTextEdit()
        input_field.setPlaceholderText("Type something...")

        font = QFont()
        font.setPointSize(24)
        input_field.setFont(font)

        layout = self.retrieve_content_layout()
        layout.addWidget(input_field)

    def initialize_control_ui(self):
        self.control_window.setWindowTitle("Controller")
        base_widget = QWidget()
        layout = QVBoxLayout(base_widget)

        dash_btn = QPushButton("Dashboard")
        dash_btn.clicked.connect(self.load_dashboard_view)
        layout.addWidget(dash_btn)

        page_btn = QPushButton("Page")
        page_btn.clicked.connect(self.load_page_view)
        layout.addWidget(page_btn)

        desktop_btn = QPushButton("Desktop")
        desktop_btn.clicked.connect(self.load_desktop_view)
        layout.addWidget(desktop_btn)

        add_text_btn = QPushButton("Insert Text Area")
        add_text_btn.clicked.connect(self.insert_text_area)
        layout.addWidget(add_text_btn)

        close_btn = QPushButton("Quit")
        close_btn.clicked.connect(self.terminate_application)
        layout.addWidget(close_btn)

        self.control_window.setCentralWidget(base_widget)
        self.control_window.resize(400, 300)
        self.control_window.show()

        available_screens = self.app_instance.screens()
        if len(available_screens) > 1:
            second_screen = available_screens[1].geometry()
            self.control_window.move(second_screen.x(), second_screen.y())

    def load_dashboard_view(self):
        self.display_window_with_content("Dashboard")

    def load_page_view(self):
        self.display_window_with_content("Page", enable_vertical_scroll=True)

    def load_desktop_view(self):
        self.display_window_with_content("Desktop", enable_horizontal_scroll=True)

    def display_window_with_content(self, title, enable_vertical_scroll=False, enable_horizontal_scroll=False):
        self.display_window.setWindowTitle(title)
        outer_widget = QWidget()
        main_layout = QVBoxLayout(outer_widget)

        info = self.generate_screen_info_label(self.app_instance.screens()[0])
        main_layout.addWidget(info)

        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)

        if enable_vertical_scroll or enable_horizontal_scroll:
            scroll_box = QScrollArea()
            scroll_box.setWidgetResizable(True)
            main_layout.addWidget(scroll_box)
            scroll_box.setWidget(content_area)
            if enable_vertical_scroll:
                scroll_box.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            if enable_horizontal_scroll:
                scroll_box.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        else:
            main_layout.addWidget(content_area)

        self.display_window.setCentralWidget(outer_widget)
        self.display_window.showFullScreen()

    def enable_dark_theme(self):
        self.app_instance.setStyle("Fusion")
        color_palette = self.app_instance.palette()
        color_palette.setColor(color_palette.ColorRole.Window, Qt.GlobalColor.black)
        color_palette.setColor(color_palette.ColorRole.WindowText, Qt.GlobalColor.white)
        self.app_instance.setPalette(color_palette)

    def start(self):
        self.app_instance.exec()


if __name__ == "__main__":
    manager = InterfaceManager()
    manager.start()
