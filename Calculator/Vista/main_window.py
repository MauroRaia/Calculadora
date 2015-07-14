# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class MainWindow (QtGui.QWidget):

    def __init__(self):
        super(MainWindow , self).__init__()
##        self.controlador = MainController
        self.init_ui()

    def init_ui(self):
        self.main_layout = QtGui.QGridLayout()
        display = QtGui.QLineEdit("0")
        display.setReadOnly(True)
        button_fv = QtGui.QPushButton("Calculadora")
        button_sv = QtGui.QPushButton("Calculadora cientifica")
        button_tv = QtGui.QPushButton("Calculadora Binaria")
        button_cv = QtGui.QPushButton("Conversor")
        self.main_layout.addWidget(display , 0, 0, 1, -1)
        self.main_box = QtGui.QVBoxLayout()
        self.main_box.addWidget(button_fv,)
        self.main_box.addWidget(button_sv,)
        self.main_box.addWidget(button_tv,)
        self.main_box.addWidget(button_cv,)
        button_sv.clicked.connect(self.hideWidget)

##First view (Normal calculator) | Primera vista (Calculadora normal)

        number_0 = QtGui.QPushButton("0")
        number_1 = QtGui.QPushButton("1")
        number_2 = QtGui.QPushButton("2")
        number_3 = QtGui.QPushButton("3")
        number_4 = QtGui.QPushButton("4")
        number_5 = QtGui.QPushButton("5")
        number_6 = QtGui.QPushButton("6")
        number_7 = QtGui.QPushButton("7")
        number_8 = QtGui.QPushButton("8")
        number_9 = QtGui.QPushButton("9")

        clear_display = QtGui.QPushButton("CE")
        dot = QtGui.QPushButton(".")
        parenthesis_o = QtGui.QPushButton("(")
        parenthesis_c = QtGui.QPushButton(")")

        button_sum = QtGui.QPushButton("+")
        button_sub = QtGui.QPushButton("-")
        button_mul = QtGui.QPushButton("*")
        button_div = QtGui.QPushButton("/")
        button_solve = QtGui.QPushButton("=")

        layout_grid = QtGui.QGridLayout()
        layout_grid.addWidget(number_1, 0, 0)
        layout_grid.addWidget(number_2, 0, 1)
        layout_grid.addWidget(number_3, 0, 2)
        layout_grid.addWidget(button_sum, 0, 3)
        layout_grid.addWidget(number_4, 1, 0)
        layout_grid.addWidget(number_5, 1, 1)
        layout_grid.addWidget(number_6, 1, 2)
        layout_grid.addWidget(button_sub, 1, 3)
        layout_grid.addWidget(number_7, 2, 0)
        layout_grid.addWidget(number_8, 2, 1)
        layout_grid.addWidget(number_9, 2, 2)
        layout_grid.addWidget(button_mul, 2, 3)
        layout_grid.addWidget(clear_display, 3, 0)
        layout_grid.addWidget(number_0, 3, 1)
        layout_grid.addWidget(dot, 3, 2)
        layout_grid.addWidget(button_div, 3, 3)
        layout_grid.addWidget(parenthesis_o, 0, 4)
        layout_grid.addWidget(parenthesis_c, 1, 4)
        layout_grid.addWidget(button_solve, 2, 4, -1 ,1)
        button_solve.setFixedHeight(64)


        self.box_fv = QtGui.QGroupBox()
        self.box_fv.setLayout(layout_grid)
        self.main_layout.addLayout(self.main_box, 1, 0, 1, 1)
        self.main_layout.addWidget(self.box_fv, 1, 1, 1, 1)
        self.setLayout(self.main_layout)
        self.show()

##Button actions | Acciones de los botones

    def hideWidget(self):
        self.box_fv.setHidden(True)

##App init

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())

