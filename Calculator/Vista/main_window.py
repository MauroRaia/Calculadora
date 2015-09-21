# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui
sys.path.append("../Controlador")
from Controller import *

class MainWindow (QtGui.QWidget):

    def __init__(self):
        super(MainWindow , self).__init__()
        self.controller = MainController(self)
        self.init_ui()
        self.signal = 0


    def init_ui(self):
        self.main_gridLayout = QtGui.QGridLayout()
        self.display = QtGui.QLineEdit("0")
        self.display.setReadOnly(True)
        button_erase = QtGui.QPushButton("X")
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
        button_erase.clicked.connect(self.controller.erase_last)

##First view | Primera vista (Listo)

        self.number_0 = QtGui.QPushButton("0")
        self.number_1 = QtGui.QPushButton("1")
        self.number_2 = QtGui.QPushButton("2")
        self.number_3 = QtGui.QPushButton("3")
        self.number_4 = QtGui.QPushButton("4")
        self.number_5 = QtGui.QPushButton("5")
        self.number_6 = QtGui.QPushButton("6")
        self.number_7 = QtGui.QPushButton("7")
        self.number_8 = QtGui.QPushButton("8")
        self.number_9 = QtGui.QPushButton("9")
        self.number_0.clicked.connect(self.controller.write)
        self.number_1.clicked.connect(self.controller.write)
        self.number_2.clicked.connect(self.controller.write)
        self.number_3.clicked.connect(self.controller.write)
        self.number_4.clicked.connect(self.controller.write)
        self.number_5.clicked.connect(self.controller.write)
        self.number_6.clicked.connect(self.controller.write)
        self.number_7.clicked.connect(self.controller.write)
        self.number_8.clicked.connect(self.controller.write)
        self.number_9.clicked.connect(self.controller.write)

        self.clear_display = QtGui.QPushButton("CE")
        self.dot = QtGui.QPushButton(".")
        self.parenthesis_open = QtGui.QPushButton("(")
        self.parenthesis_close = QtGui.QPushButton(")")
        self.clear_display.clicked.connect(self.controller.clear)
        self.dot.clicked.connect(self.controller.write)
        self.parenthesis_open.clicked.connect(self.controller.write)
        self.parenthesis_close.clicked.connect(self.controller.write)

        self.button_sum = QtGui.QPushButton("+")
        self.button_sub = QtGui.QPushButton("-")
        self.button_mul = QtGui.QPushButton("*")
        self.button_div = QtGui.QPushButton("/")
        self.button_solve = QtGui.QPushButton("=")
        self.button_sum.clicked.connect(self.controller.write)
        self.button_sub.clicked.connect(self.controller.write)
        self.button_mul.clicked.connect(self.controller.write)
        self.button_div.clicked.connect(self.controller.write)
        self.button_solve.clicked.connect(lambda: self.controller.do(self.display.text()))

        layout_grid_fv = QtGui.QGridLayout()
        layout_grid_fv.addWidget(self.number_1, 0, 0)
        layout_grid_fv.addWidget(self.number_2, 0, 1)
        layout_grid_fv.addWidget(self.number_3, 0, 2)
        layout_grid_fv.addWidget(self.button_sum, 0, 3)
        layout_grid_fv.addWidget(self.number_4, 1, 0)
        layout_grid_fv.addWidget(self.number_5, 1, 1)
        layout_grid_fv.addWidget(self.number_6, 1, 2)
        layout_grid_fv.addWidget(self.button_sub, 1, 3)
        layout_grid_fv.addWidget(self.number_7, 2, 0)
        layout_grid_fv.addWidget(self.number_8, 2, 1)
        layout_grid_fv.addWidget(self.number_9, 2, 2)
        layout_grid_fv.addWidget(self.button_mul, 2, 3)
        layout_grid_fv.addWidget(self.clear_display, 3, 0)
        layout_grid_fv.addWidget(self.number_0, 3, 1)
        layout_grid_fv.addWidget(self.dot, 3, 2)
        layout_grid_fv.addWidget(self.button_div, 3, 3)
        layout_grid_fv.addWidget(self.parenthesis_open, 0, 4)
        layout_grid_fv.addWidget(self.parenthesis_close, 1, 4)
        layout_grid_fv.addWidget(self.button_solve, 2, 4, -1, 1)
        self.button_solve.setFixedHeight(64)


        self.box_fv = QtGui.QGroupBox()
        box_fv_1 = QtGui.QGridLayout()
        box_fv_1.addLayout(layout_grid_fv, 0, 0, 1, 1)


## Second view | Segunda vista (Listo)

        self.button_log = QtGui.QPushButton("Log")
        self.button_cos = QtGui.QPushButton("Cos")
        self.button_sin = QtGui.QPushButton("Sin")
        self.button_tan = QtGui.QPushButton("Tan")
        self.button_squareRoot = QtGui.QPushButton("√")
        self.button_exponent = QtGui.QPushButton("χ²")
        self.button_exponentX = QtGui.QPushButton("Y˟")
        self.button_log.clicked.connect(self.controller.write)
        self.button_cos.clicked.connect(self.controller.write)
        self.button_sin.clicked.connect(self.controller.write)
        self.button_tan.clicked.connect(self.controller.write)
        self.button_squareRoot.clicked.connect(self.controller.write)
        self.button_exponent.clicked.connect(self.controller.write)
        self.button_exponentX.clicked.connect(self.controller.write)

        self.box_sv = QtGui.QGroupBox()
        box_sv_1 = QtGui.QGridLayout()
        box_sv_1.addWidget(self.button_log, 0, 0, 1, 1)
        box_sv_1.addWidget(self.button_cos, 1, 0, 1, 1)
        box_sv_1.addWidget(self.button_sin, 0, 1, 1, 1)
        box_sv_1.addWidget(self.button_tan, 1, 1, 1, 1)
        box_sv_1.addWidget(self.button_squareRoot, 0, 2, 1, 1)
        box_sv_1.addWidget(self.button_exponent, 1, 2, 1, 1)
        box_sv_1.addWidget(self.button_exponentX, 0, 3, 1, 1)

        self.box_sv.setHidden(True)
        self.box_fv.setLayout(box_fv_1)
        self.box_sv.setLayout(box_sv_1)
        box_fv_1.addWidget(self.box_sv)

## Third view | Tercera vista

        self.first_bin = QtGui.QLineEdit("Ingresar primer binario")
        self.second_bin = QtGui.QLineEdit("Ingresar segundo binario")
        self.binary_sum = QtGui.QPushButton("+")
        self.binary_sub = QtGui.QPushButton("-")
        self.binary_mul = QtGui.QPushButton("*")
        self.binary_div = QtGui.QPushButton("/")
        self.binary_solve = QtGui.QPushButton("=")

        self.binary_sum.clicked.connect(self.controller.do_binary)
        self.binary_sub.clicked.connect(self.controller.do_binary)
        self.binary_mul.clicked.connect(self.controller.do_binary)
        self.binary_div.clicked.connect(self.controller.do_binary)
        self.binary_solve.clicked.connect(self.controller.do_binary)

        box_tv_1 = QtGui.QGridLayout()
        box_tv_1.addWidget(self.binary_sum, 0, 0, 1, 1)
        box_tv_1.addWidget(self.binary_sub, 1, 0, 1, 1)
        box_tv_1.addWidget(self.binary_mul, 0, 1, 1, 1)
        box_tv_1.addWidget(self.binary_div, 0, 2, 1, 1)
        box_tv_1.addWidget(self.binary_solve, 1, 2, 1, 1)
        box_tv_1.addWidget(self.first_bin, 2, 0, 1, -1)
        box_tv_1.addWidget(self.second_bin, 3, 0, 1, -1)
        self.binary_solve.setFixedHeight(32)


        self.box_tv = QtGui.QGroupBox()
        self.box_tv.setLayout(box_tv_1)
        self.box_tv.setHidden(True)


## Converter | Conversor (Listo)

        button_dec = QtGui.QPushButton("Convertir a decimal")
        button_bin = QtGui.QPushButton("Convertir a binario")
        self.input_text = QtGui.QLineEdit("Inserte el numero a convertir")

        layout_grid_cv = QtGui.QGridLayout()
        layout_grid_cv.addWidget(self.input_text)
        layout_grid_cv.addWidget(button_dec)
        layout_grid_cv.addWidget(button_bin)

        button_bin.clicked.connect(self.controller.int_to_bin)
        button_dec.clicked.connect(self.controller.bin_to_int)

        self.box_cv = QtGui.QGroupBox()
        self.box_cv.setLayout(layout_grid_cv)
        self.box_cv.setHidden(True)

##Integración de boxes al main_gridLayout

        self.main_gridLayout.addWidget(self.display, 0, 1, 1, 1)
        button_erase.setFixedWidth(32)
        self.main_gridLayout.addWidget(button_erase, 0, 0, 1, 1, Qt.AlignRight)
        self.main_gridLayout.addLayout(self.main_verticalLayout, 1, 0, 1, 1)

        self.main_gridLayout.addWidget(self.box_fv, 1, 1, 1, 1)
        self.main_gridLayout.addWidget(self.box_cv, 1, 1, 1, 1)
        self.main_gridLayout.addWidget(self.box_tv, 1, 1, 1, 1)
        self.setLayout(self.main_gridLayout)
        self.show()

##TECLAS

    def keyPressEvent(self, e):
        value = str(e.text())
        text_d = (str(self.display.text())) + value
        if  (str(self.display.text())) == "0":
            self.display.setText(value)
        else:
            self.display.setText(text_d)


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
