'''
David Würfl
09.02.2023#
###############
Piero Barboza Bidner
22.02.2023
Game-Function
'''
'''
        self.save_action = QtGui.QAction("Save", self)
        self.save_action.triggered.connect(self.save_score)
        self.file_menu.addAction(self.save_action)

        self.load_action = QtGui.QAction("Load", self)
        self.load_action.triggered.connect(self.load_game)
        self.file_menu.addAction(self.load_action)
'''
import sys
import random
from PyQt6 import QtGui
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Memory")
        self.setFixedSize(QSize(700, 900))
        
        level = 1
        self.set_size(level)
        self.safefile = False
        
        self.menu = self.menuBar()
        self.options_menu = self.menu.addMenu("Options")
        self.size_menu = self.menu.addMenu("Field-Size")

        self.quit_action = QtGui.QAction("Quit", self)
        self.quit_action.triggered.connect(QApplication.instance().quit)
        self.options_menu.addAction(self.quit_action)
        
        self.quit_action = QtGui.QAction("Reset", self)
        self.quit_action.triggered.connect(lambda:self.set_size(level=1))
        self.options_menu.addAction(self.quit_action)
        
        self.small_action = QtGui.QAction("Small", self)
        self.small_action.triggered.connect (lambda:self.set_size(1, True))
        self.size_menu.addAction(self.small_action)

        self.medium_action = QtGui.QAction("Medium", self)
        self.medium_action.triggered.connect(lambda: self.set_size(2, True))
        self.size_menu.addAction(self.medium_action)

        self.big_action = QtGui.QAction("Big", self)
        self.big_action.triggered.connect(lambda: self.set_size(3, True))
        self.size_menu.addAction(self.big_action)
        
    
    def set_size(self, level, reset=False):
     
        if(level == 1):
            self.size = 6
            self.sizeb = 4
            self.button_size = 135
            self.button_sizeb = 169
            self.memory()
            
        elif(level == 2):
            self.size = 6
            self.sizeb = 5
            self.button_size = 135
            self.button_sizeb = 135
            self.memory()
            
        elif(level == 3):
            self.size = 7
            self.sizeb = 6
            self.button_size = 116
            self.button_sizeb = 113
            self.memory()

    def memory(self):
        
        self.Layout = QGridLayout()
        self.buttons = []
        for i in range(self.size):
            for j in range(self.sizeb):
                
                self.button = QPushButton("")
                self.buttons.append(self.button)
                self.Layout.addWidget(self.button,i,j)
                self.button.setFixedSize(self.button_sizeb, self.button_size)
                self.Layout.addWidget(self.button,i,j)
        
        widget = QWidget()
        widget.setLayout(self.Layout)
        self.setCentralWidget(widget)
        
        self.widget_1 = QLabel("Tries: ")
        font = self.widget_1.font()
        font.setPointSize(15)
        self.widget_1.setFont(font)
        self.widget_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.widget_1,7,0)
        
        self.widget_2 = QLabel("Pairs left: ")
        font = self.widget_2.font()
        font.setPointSize(15)
        self.widget_2.setFont(font)
        self.widget_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.widget_2,7,2)
      
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()    