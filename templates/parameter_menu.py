from PySide6.QtWidgets import (QLabel, QWidget, QDoubleSpinBox, QComboBox, QPushButton,
                                QHBoxLayout, QVBoxLayout)


class MultiWidget(QWidget):
    """
    This will take a dictionary of parameters and generate 
    a vertical layout of widgets to set their values.
    """
    def __init__(self, parent=None, **params):
        super().__init__()
        self.setGeometry(900, 400, 200, 100)
        self.parent = parent
        self._widgets = {}
        self.values = params
        self.change_button = QPushButton("Accept New Values")
        self.load_form()
        self.set_layout()

    def load_form(self):
        """
        Load in each single widget
        """
        for key in self.values.keys():
            self._widgets[key] = SingleWidget(self,key ,**self.values[key])

    def set_layout(self):
        """
        Set the main (MultiWidget) layout and add all child widgets
        """
        layout = QVBoxLayout()    
        for key in self._widgets.keys():
            layout.addWidget(self._widgets[key])
        layout.addWidget(self.change_button)
        self.setLayout(layout)


class SingleWidget(QWidget):
    """
    Create a single widget: title box with associated value changer.
    """
    def __init__(self, parent=None, property=None, **values):
        super().__init__()
        self.values, self.parent = values, parent
        self.property = property
        self.layout = QHBoxLayout()
        self.make_label()
        self.make_widget()
        self.setLayout(self.layout)

        #Here if one presses a button the parameter info. updates.
        self.parent.change_button.clicked.connect(self.connect)

    def make_label(self):
        if "title" in self.values.keys():
            label = QLabel(self.values["title"])
            self.layout.addWidget(label)

    def make_widget(self):
        type = self.values["type"]
        if type == "bool":
            self.instance = BoolWidget(self, **self.values)
        if type == "int":
            self.instance = IntWidget(self, **self.values)
        if type == "float":
            self.instance = FloatWidget(self, **self.values)
        if type == "str":
            self.instance = StrWidget(self, **self.values)

    def connect(self):
        """
        When values are changed send new data back to parent.
        """
        self.instance._connect()
        self.parent.values[self.property] = self.values
        print("changed")


    def __getattr__(self, name):
        return self.instance.__getattribute__(name)


class BoolWidget(QWidget):
    """
    A boolean QComboBox
    """
    def __init__(self, parent=None, **values):
        super().__init__()
        self.parent = parent
        self.values = values
        self.main_widget()

    def main_widget(self):
        self.widget = QComboBox()
        items = ["False", "True"]
        [self.widget.addItem(i) for i in items]
        self.parent.layout.addWidget(self.widget)
    
    def _connect(self):
        """
        On change send new value back to parent
        """
        new_val = self.widget.currentText()
        if new_val == "True":
            new_val = True
        if new_val == "False":
            new_val = False
        self.value = new_val
        self.values["value"] = new_val
        self.parent.values = self.values


class IntWidget(QWidget):
    """
    A QDoubleSpinBox with integer values.
    """
    def __init__(self, parent=None, **values):
        super().__init__()
        self.parent = parent
        self.values = values
        self.min, self.max = 0, 100
        self.valstep, self.value = 1, 0
        self.set_values(**values)
        self.main_widget()
        

    def set_values(self, **values):
        for key in values.keys():
            self.__setattr__(key, values[key])

    def main_widget(self):
        self.widget = QDoubleSpinBox(minimum=self.min, maximum=self.max,
                                     singleStep=self.valstep,
                                     value=self.value)
        self.parent.layout.addWidget(self.widget)
    
    def _connect(self):
        """
        On change update the parent's parameter values.
        """
        new_val = int(self.widget.value())
        self.value = new_val
        self.values["value"] = new_val
        self.parent.values = self.values


class FloatWidget(QWidget):
    """
    QDoubleSpinBox for floating point numbers.
    """
    def __init__(self, parent=None, **values):
        super().__init__()
        self.parent = parent
        self.min, self.max = 0, 100
        self.values = values
        self.valstep, self.value = 0.1, 0
        self.set_values(**values)
        self.main_widget()

    def set_values(self, **values):
        for key in values.keys():
            self.__setattr__(key, values[key])

    def main_widget(self):
        self.widget = QDoubleSpinBox(minimum=self.min, maximum=self.max,
                                     singleStep=self.valstep,
                                     value=self.value)
        self.parent.layout.addWidget(self.widget)

    def _connect(self):
        new_val = float(self.widget.value())
        self.value = new_val
        self.values["value"] = new_val
        self.parent.values = self.values


class StrWidget(QWidget):
    """
    QComboBox for string value selection.
    """
    def __init__(self, parent=None, **values):
        super().__init__()
        self.parent = parent
        self.values = values
        self.enum, self.idx = [], 0
        self.set_values(**values)
        self.main_widget()

    def set_values(self, **values):
        for key in values.keys():
            self.__setattr__(key, values[key])

    def main_widget(self):
        self.widget = QComboBox()
        if hasattr(self, "value"):
            self.idx = self.enum.index(self.value)
        [self.widget.addItem(i) for i in self.enum]
        self.parent.layout.addWidget(self.widget)
        self.widget.setCurrentIndex(self.idx)

    def _connect(self):
        new_val = self.widget.currentText()
        self.value = new_val
        self.values["value"] = new_val
        self.parent.values = self.values
