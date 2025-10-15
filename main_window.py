from PySide6.QtWidgets import (QMainWindow, QApplication)
from templates.example_forms import StartingParams
from main_widget import MainWidget

import sys

class Win(QMainWindow):
    """
    Main window to add the child MultiWidget to
    """
    def __init__(self, **params):
        super().__init__()
        self.setGeometry(100, 100, 600, 500)

        self.widget = MainWidget(parent=self, params=params)
        self.setCentralWidget(self.widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win(**StartingParams)
    win.show()
 

    app.exec()