# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class MainWindow (QtGui.QWidget):

    def __init__(self):
        super(MainWindow , self).__init__()
##        self.controlador = MainController
        self.init_ui()

    def init_ui(self):
        self.main_gridLayout = QtGui.QGridLayout()
        display = QtGui.QLineEdit("0")
        display.setReadOnly(True)
        button_fv = QtGui.QPushButton("Calculadora")
        button_sv = QtGui.QPushButton("Calculadora cientifica")
        button_tv = QtGui.QPushButton("Calculadora Binaria")
        button_cv = QtGui.QPushButton("Conversor")
        self.main_verticalLayout = QtGui.QVBoxLayout()
        self.main_verticalLayout.addWidget(button_fv,)
        self.main_verticalLayout.addWidget(button_sv,)
        self.main_verticalLayout.addWidget(button_tv,)
        self.main_verticalLayout.addWidget(button_cv,)
        button_fv.clicked.connect(self.showFV)
        button_sv.clicked.connect(self.showSV)
        button_cv.clicked.connect(self.showCV)
        button_tv.clicked.connect(self.showTV)

##First view | Primera vista (Listo)

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

        layout_grid_fv = QtGui.QGridLayout()
        layout_grid_fv.addWidget(number_1, 0, 0)
        layout_grid_fv.addWidget(number_2, 0, 1)
        layout_grid_fv.addWidget(number_3, 0, 2)
        layout_grid_fv.addWidget(button_sum, 0, 3)
        layout_grid_fv.addWidget(number_4, 1, 0)
        layout_grid_fv.addWidget(number_5, 1, 1)
        layout_grid_fv.addWidget(number_6, 1, 2)
        layout_grid_fv.addWidget(button_sub, 1, 3)
        layout_grid_fv.addWidget(number_7, 2, 0)
        layout_grid_fv.addWidget(number_8, 2, 1)
        layout_grid_fv.addWidget(number_9, 2, 2)
        layout_grid_fv.addWidget(button_mul, 2, 3)
        layout_grid_fv.addWidget(clear_display, 3, 0)
        layout_grid_fv.addWidget(number_0, 3, 1)
        layout_grid_fv.addWidget(dot, 3, 2)
        layout_grid_fv.addWidget(button_div, 3, 3)
        layout_grid_fv.addWidget(parenthesis_o, 0, 4)
        layout_grid_fv.addWidget(parenthesis_c, 1, 4)
        layout_grid_fv.addWidget(button_solve, 2, 4, -1, 1)
        button_solve.setFixedHeight(64)


        self.box_fv = QtGui.QGroupBox()
        box_fv_1 = QtGui.QGridLayout()
        box_fv_1.addLayout(layout_grid_fv, 0, 0, 1, 1)


## Second view | Segunda vista (Listo)

        button_log = QtGui.QPushButton("Log")
        button_cos = QtGui.QPushButton("Cos")
        button_sin = QtGui.QPushButton("Sin")
        button_tan = QtGui.QPushButton("Tan")
        button_squareRoot = QtGui.QPushButton("√")
        button_exponent = QtGui.QPushButton("χ²")
        button_exponentX = QtGui.QPushButton("Y˟")

        self.box_sv = QtGui.QGroupBox()
        box_sv_1 = QtGui.QGridLayout()
        box_sv_1.addWidget(button_log, 0, 0, 1, 1)
        box_sv_1.addWidget(button_cos, 1, 0, 1, 1)
        box_sv_1.addWidget(button_sin, 0, 1, 1, 1)
        box_sv_1.addWidget(button_tan, 1, 1, 1, 1)
        box_sv_1.addWidget(button_squareRoot, 0, 2, 1, 1)
        box_sv_1.addWidget(button_exponent, 1, 2, 1, 1)
        box_sv_1.addWidget(button_exponentX, 0, 3, 1, 1)

        self.box_sv.setHidden(True)
        self.box_fv.setLayout(box_fv_1)
        self.box_sv.setLayout(box_sv_1)
        box_fv_1.addWidget(self.box_sv)

## Third view | Tercera vista

        binary_1 = QtGui.QPushButton("1")
        binary_2 = QtGui.QPushButton("2")
        binary_sum = QtGui.QPushButton("+")
        binary_sub = QtGui.QPushButton("-")
        binary_mul = QtGui.QPushButton("*")
        binary_div = QtGui.QPushButton("/")
        binary_solve = QtGui.QPushButton("=")

        box_tv_1 = QtGui.QGridLayout()
        box_tv_1.addWidget(binary_1, 0, 0, -1, 1)
        box_tv_1.addWidget(binary_2, 0, 1, -1, 1)
        box_tv_1.addWidget(binary_sum, 0, 2, 1, 1)
        box_tv_1.addWidget(binary_sub, 1, 2, 1, 1)
        box_tv_1.addWidget(binary_mul, 2, 2, 1, 1)
        box_tv_1.addWidget(binary_div, 3, 2, 1, 1)
        box_tv_1.addWidget(binary_solve, 0, 3, -1, 1)
        binary_1.setFixedHeight(128)
        binary_2.setFixedHeight(128)
        binary_solve.setFixedHeight(128)

        self.box_tv = QtGui.QGroupBox()
        self.box_tv.setLayout(box_tv_1)
        self.box_tv.setHidden(True)


## Converter | Conversor (Listo)

        button_dec = QtGui.QPushButton("Convertir a decimal")
        button_bin = QtGui.QPushButton("Convertir a binario")
        input_text = QtGui.QLineEdit("Inserte el numero a convertir")

        layout_grid_cv = QtGui.QGridLayout()
        layout_grid_cv.addWidget(input_text)
        layout_grid_cv.addWidget(button_dec)
        layout_grid_cv.addWidget(button_bin)

        self.box_cv = QtGui.QGroupBox()
        self.box_cv.setLayout(layout_grid_cv)
        self.box_cv.setHidden(True)

##Integración de boxes al main_gridLayout

        self.main_gridLayout.addWidget(display, 0, 0, 1, -1)
        self.main_gridLayout.addLayout(self.main_verticalLayout, 1, 0, 1, 1)

        self.main_gridLayout.addWidget(self.box_fv, 1, 1, 1, 1)
        self.main_gridLayout.addWidget(self.box_cv, 1, 1, 1, 1)
        self.main_gridLayout.addWidget(self.box_tv, 1, 1, 1, 1)
        self.setLayout(self.main_gridLayout)
        self.show()

##Button actions | Acciones de los botones

    def showFV(self):
        self.box_fv.setHidden(False)
        self.box_sv.setHidden(True)
        self.box_cv.setHidden(True)
        self.box_tv.setHidden(True)

    def showSV(self):
        self.box_fv.setHidden(False)
        self.box_sv.setHidden(False)
        self.box_cv.setHidden(True)
        self.box_tv.setHidden(True)

    def showTV(self):
        self.box_fv.setHidden(True)
        self.box_sv.setHidden(True)
        self.box_cv.setHidden(True)
        self.box_tv.setHidden(False)

    def showCV(self):
        self.box_fv.setHidden(True)
        self.box_sv.setHidden(True)
        self.box_cv.setHidden(False)
        self.box_tv.setHidden(True)

##App init

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
