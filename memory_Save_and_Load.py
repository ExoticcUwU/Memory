'''
Exoticc
22.02.2023
Updated memory game with 'Save' and 'Load' options
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
        self.setFixedSize(QSize(900, 700))
        
        self.set_size(1)
        self.safefile = False
        
        self.menu = self.menuBar()
        self.file_menu =self.menu.addMenu("File")
        self.options_menu = self.menu.addMenu("Options")
        self.size_menu = self.menu.addMenu("Field-Size")

        self.save_action=QtGui.QAction("Save",self)
        self.save_action.triggered.connect(self.save_score)
        self.file_menu.addAction(self.save_action)

        self.load_action=QtGui.QAction("Load", self)
        self.load_action.triggered.connect(self.load_game)
        self.file_menu.addAction(self.load_action)

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
        self.diff=level
     
        if(level == 1):
            self.size = 6
            self.sizeb = 4
            self.button_size = 103
            self.button_sizeb = 220
            self.memory()
            
        elif(level == 2):
            self.size = 6
            self.sizeb = 5
            self.button_size = 103
            self.button_sizeb = 176
            self.memory()
            
        elif(level == 3):
            self.size = 7
            self.sizeb = 6
            self.button_size = 88
            self.button_sizeb = 146
            self.memory()

    def memory(self):
        self.num_tries =0
        self.num_pairs =int((self.size *self.sizeb)/2) #math :|
        self.level =self.diff

        self.Layout = QGridLayout()
        self.buttons = []
        for i in range(self.size):
            for j in range(self.sizeb):
                
                self.button = QPushButton("")
                self.buttons.append(self.button)
                self.Layout.addWidget(self.button,i,j)
                self.button.setFixedSize(self.button_sizeb, self.button_size)

        widget = QWidget()
        widget.setLayout(self.Layout)
        self.setCentralWidget(widget)
        
        self.widget_1 = QLabel(f"Tries:{self.num_tries}")
        font = self.widget_1.font()
        font.setPointSize(15)
        self.widget_1.setFont(font)
        self.widget_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.widget_1,7,0)
        
        self.widget_2 = QLabel(f"Pairs left:{self.num_pairs}")
        font = self.widget_2.font()
        font.setPointSize(15)
        self.widget_2.setFont(font)
        self.widget_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.widget_2,7,2)

    def save_score(self): #save function
        save_objects =f"{self.diff,self.num_tries,self.num_pairs}" #creats a string which holds all necessary values
        file_name =QFileDialog.getSaveFileName(self) #get file name
        with open(file_name[0], "w+") as fobj: #write in and overwrite if saved on to again
            fobj.write(save_objects) 

    def load_game(self): #load function
        file_name =QFileDialog.getOpenFileName(self)
        with open (file_name[0], "r") as fobj:
            readIn =fobj.readline() #reads the complete line and return it as a string
        self.diff =int(readIn[1])
        self.num_tries =int(readIn[readIn.index(",")+2]) #read in index at given postion ',+2' =5
        self.num_pairs =int(readIn[readIn.index(")")-1])

        self.widget_2 =QLabel(f"Pairs left:{self.num_pairs}")#updating the labels to the loaded in values
        self.widget_1 =QLabel(f"Tries:{self.num_tries}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()    
