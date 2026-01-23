import sys
import os

from paths import Path
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.url.setPlaceholderText("Insert full url here")
        self.btn = QPushButton("Set thumbnail")

        self.label = QLabel()

        layout.addWidget(self.url)
        layout.addWidget(self.btn)
        layout.addWidget(self.label)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
