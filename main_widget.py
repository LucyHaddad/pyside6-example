from PySide6.QtWidgets import (QWidget, QVBoxLayout,
                               QPushButton)
from plotting_widget import BasicPlot
from templates.parameter_menu import MultiWidget

class MainWidget(QWidget):
    def __init__(self, parent=None, params=None):
        super(MainWidget, self).__init__(parent)
        self.params = params

        layout = QVBoxLayout()
        self.pushbutton = QPushButton("Press for menu")
        self.plot_widget = BasicPlot(self)
        self.plot_widget.setLayout(self.plot_widget.layout)

        [layout.addWidget(w) for w in [self.plot_widget, self.pushbutton]]
        self.setLayout(layout)

        #connect the push button to show the MultiWidget
        self.pushbutton.pressed.connect(self.open_params)
        #may need to press it twice..
    
    def open_params(self):
        self.menu = MultiWidget(parent=self, **self.params)
        self.menu.show()
        self.menu.change_button.pressed.connect(self.on_param_change)

    def on_param_change(self):
        vals = self.menu.values
        if vals["BoolChoice"]["value"] == True:
            self.plot_widget.canvas.ax.set_title("TRUE")
            self.plot_widget.canvas.draw_idle()
