import sys
import os

from paths import Path
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
