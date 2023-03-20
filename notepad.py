import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout


class Notepad(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.clear_button = QPushButton("Clear")
        self.open_button = QPushButton("Open")
        self.save_button = QPushButton("Save")

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.clear_button)
        horizontal_layout.addWidget(self.open_button)
        horizontal_layout.addWidget(self.save_button)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.text_edit)
        vertical_layout.addLayout(horizontal_layout)

        self.setLayout(vertical_layout)

        self.setWindowTitle("Notepad")
        self.clear_button.clicked.connect(self.clear_text)
        self.open_button.clicked.connect(self.open_file)
        self.save_button.clicked.connect(self.save_file)

        self.show()

    def clear_text(self):
        self.text_edit.clear()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))
        if file_name:
            try:
                with open(file_name, "r") as f:
                    self.text_edit.setText(f.read())
            except Exception as e:
                print(f"Error opening file: {e}")

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))
        if file_name:
            try:
                with open(file_name, "w") as f:
                    f.write(self.text_edit.toPlainText())
            except Exception as e:
                print(f"Error saving file: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())
