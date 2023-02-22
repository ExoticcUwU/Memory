'''
David Würfl
09.02.2023
Layout
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
import time
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
            self.color_list = ['Violet', 'Silver', 'Blue', 'Steelblue', 
                               'Crimson', 'Peru', 'Orange', 'Tan', 
                               'Gold', 'Coral', 'Pink', 'Maroon']
            self.memory()
            
        elif(level == 2):
            self.size = 6
            self.sizeb = 5
            self.button_size = 135
            self.button_sizeb = 135
            self.color_list = ['Violet', 'Silver', 'Blue', 'Steelblue', 'Crimson',
                               'Peru', 'Orange', 'Tan', 'Gold', 'Coral', 
                               'Pink', 'Maroon', 'Green', 'Beige', 'Indigo']
            self.memory()
            
        elif(level == 3):
            self.size = 7
            self.sizeb = 6
            self.button_size = 116
            self.button_sizeb = 113
            self.color_list = ['Violet', 'Silver', 'Blue', 'Steelblue', 'Crimson',
                               'Peru', 'Orange', 'Tan', 'Gold', 'Coral', 'Pink',
                               'Maroon', 'Green', 'Beige', 'Indigo', 'Olive',
                               'Lime', 'Cornflower Blue', 'Teal', 'Turquoise','Magenta']
            self.memory()

    def memory(self):
        
        self.Layout = QGridLayout()

        self.color_list.extend(self.color_list)
        random.shuffle(self.color_list)
        self.digits = []
        self.counter_clicked = 0
        #print(self.color_list)
        
        self.buttons = []
        for i in range(self.size):
            for j in range(self.sizeb):
                
                self.button = QPushButton("")
                self.button.clicked.connect(lambda checked, button=self.button: self.show_color(button))
                self.buttons.append(self.button)
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
      
    def show_color(self, button):
        clicked_button = self.sender()
        cords = self.buttons.index(clicked_button)
        self.digits.append(cords)

        button.setStyleSheet(f"background-color: {self.color_list[cords]}")
        self.counter_clicked +=1

        if self.counter_clicked == 2:
            if cords == self.digits[0]:
                del self.digits[1]
                self.counter_clicked -= 1
            else:
                b = self.check()
                if b == True:
                    for x in range(2):
                        button = self.buttons[self.digits[x]]
                        button.setEnabled(False)
                    self.digits.clear()
                    self.counter_clicked = 0

                if b == False:
                    time.sleep(5)
                    for x in range(2):
                        button = self.buttons[self.digits[x]]
                        button.setStyleSheet("background-color: none")
                    self.digits.clear()
                    self.counter_clicked = 0

        while self.counter_clicked == 3:
                button.setStyleSheet("background-color: none")
                self.counter_clicked -= 1
                del self.digits[2]

    def check(self):
        if self.color_list[self.digits[0]] != self.color_list[self.digits[1]]:
            return False
        else:
            return True

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()    