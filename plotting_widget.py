from PySide6.QtWidgets import (QWidget, QVBoxLayout)
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np


class MplCanvas(FigureCanvasQTAgg):
    """
    Matplotlib canvas using Qt5Agg backend
    """
    def __init__(self, width=400, height=400):

        fig = Figure(figsize=(width, height))

        self.ax = fig.add_subplot()
        super().__init__(fig)

class BasicPlot(QWidget):
    def __init__(self, parent=None):
        super(BasicPlot, self).__init__(parent)
        self.setGeometry(0, 0, 400, 400)
        self.parent = parent

        self.layout = QVBoxLayout()
        self.canvas = MplCanvas()
        toolbar = NavigationToolbar2QT(self.canvas, self)
        self.layout.addWidget(toolbar)
        self.layout.addWidget(self.canvas)

       

    def plot_random(self):
        self.canvas.ax.plot(np.random.random_integers(0, 1000, 100))
        self.canvas.draw_idle()