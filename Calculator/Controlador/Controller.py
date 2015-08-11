# -*- coding: utf-8 -*-

import sys
sys.path.append("../Modelo")
from Logic_Unit import *


class MainController():

    def __init__(self, window):
        self.logicUnit = Logic_Unit()
        self.window = window
        self.position = 0
        self.parh_position_1 = 0
        self.parh_position_2 = 0


# def donde se capta la señal del boton apretado en la vista y se obtiene
# el texto del mismo, el cual reemplaza o complementa al texto actual
# en el display

    def write(self):
        starter = str(self.window.display.text())
        self.sender = self.window.sender()
        text_2 = str(self.sender.text())
        text = str(self.window.display.text())
        if  starter == "0":
            self.window.display.setText(text_2)
        else:
            text_3 = text + text_2
            self.window.display.setText(text_3)

    def clear(self):
        self.window.display.setText("0")

