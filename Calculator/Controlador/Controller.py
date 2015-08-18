# -*- coding: utf-8 -*-

import sys
sys.path.append("../Modelo")
from Logic_Unit import *


class MainController():

    def __init__(self, window):
        self.logicUnit = Logic_Unit()
        self.window = window
        self.position_o = 0
        self.position_1 = 0
        self.position_2 = 0
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

    def do(self, text_f):

        if (text_f.rfind("(")) != -1:
            self.parh_position_1 = text_f.rfind("(")
            self.parh_position_2 = text_f.find(")")
            string_2 = (text_f[self.parh_position_1 : (self.parh_position_2 + 1)])
            print (string_2)
            text_2 = text_f.replace((str(string_2)), (str(self.operation(string_2))), 1)
            print (text_2)
            self.do(text_2)
        else:
            text_2 = self.operation(text_f)
            self.window.display.setText(text_2)
            self.window.display.update()

    def operation(self, text):
        if (text.find("+")) != -1:
            self.position_o = text.find("+")
            print (text[self.position_o + 1])
            print (text[self.position_o])
            num_1 = int(text[self.position_o - 1])
            num_2 = int(text[self.position_o + 1])
            resultado = (num_1 + num_2)
            text_replace = (text[(self.position_o - 1) : (self.position_o + 2)])
            text_2 = text.replace(str(text_replace), str(resultado), 1)
            self.operation(text_2)
        elif (text.find("*")) != -1:
            self.position_o = text.find("*")
            num_1 = int(text[self.position_o - 1])
            num_2 = int(text[self.position_o + 1])
            print (num_1)
            print (num_2)
            resultado = (num_1 * num_2)
            text_replace = (text[(self.position_o - 1) : (self.position_o + 2)])
            text_2 = text.replace(str(text_replace), str(resultado), 1)
            print (text_2)
            self.operation(text_2)
        else:
            return text



