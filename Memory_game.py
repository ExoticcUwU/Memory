'''
David Würfl
09.02.2023
Layout
###############
Piero Barboza Bidner
22.02.2023
Game-Function
###############
Exoticc
23.02.2023
SaveAndLoad
'''

import sys
import random
from PyQt6 import QtGui
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #sets title
        self.setWindowTitle("Memory")
        #sets windowsize
        self.setFixedSize(QSize(900, 700))
        #sets starting field-size
        self.set_size(1)
        self.safefile = False
        
        #creates menu bar
        self.menu = self.menuBar()
        self.file_menu =self.menu.addMenu("File")
        self.options_menu = self.menu.addMenu("Options")
        self.size_menu = self.menu.addMenu("Field-Size")

        self.save_action=QtGui.QAction("Save",self)
        #runs the save_score function
        self.save_action.triggered.connect(self.save_score)
        self.file_menu.addAction(self.save_action)

        self.load_action=QtGui.QAction("Load", self)
        #runs the load_game function
        self.load_action.triggered.connect(self.load_game)
        self.file_menu.addAction(self.load_action)

        self.quit_action = QtGui.QAction("Quit", self)
        #closes the window 
        self.quit_action.triggered.connect(QApplication.instance().quit)
        self.options_menu.addAction(self.quit_action)
        
        self.quit_action = QtGui.QAction("Reset", self)
        #sets field-size back to small
        self.quit_action.triggered.connect(lambda:self.set_size(level=1))
        self.options_menu.addAction(self.quit_action)
        
        self.small_action = QtGui.QAction("Small", self)
        #sets field-size to small
        self.small_action.triggered.connect (lambda:self.set_size(1, True))
        self.size_menu.addAction(self.small_action)

        self.medium_action = QtGui.QAction("Medium", self)
        #sets field-size to medium
        self.medium_action.triggered.connect(lambda: self.set_size(2, True))
        self.size_menu.addAction(self.medium_action)

        self.big_action = QtGui.QAction("Big", self)
        #sets field-size to big
        self.big_action.triggered.connect(lambda: self.set_size(3, True))
        self.size_menu.addAction(self.big_action)

    def set_size(self, level, reset=False):
        self.diff =level
        
        #defines size and ammount of buttons for small playfield
        if(level == 1):
            #amount of buttons placed on y-axis
            self.size = 6
            #amount of buttons placed on x-axis
            self.sizeb = 4
            #y-size of buttons
            self.button_size = 103
            #x-size of buttons
            self.button_sizeb = 220
            #list with the colours used on this playfield-size
            self.color_list = ['Violet', 'Silver', 'Blue', 'Steelblue', 
                               'Crimson', 'Peru', 'Orange', 'Tan', 
                               'Gold', 'Coral', 'Pink', 'Maroon']
            self.memory()
            
        #defines size and ammount of buttons for medium playfield    
        elif(level == 2):
            self.size = 6
            self.sizeb = 5
            self.button_size = 103
            self.button_sizeb = 176
            self.color_list = ['Violet', 'Silver', 'Blue', 'Steelblue', 'Crimson',
                               'Peru', 'Orange', 'Tan', 'Gold', 'Coral', 
                               'Pink', 'Maroon', 'Green', 'Beige', 'Indigo']
            self.memory()
        
        #defines size and ammount of buttons for big playfield
        elif(level == 3):
            self.size = 7
            self.sizeb = 6
            self.button_size = 88
            self.button_sizeb = 146
            self.color_list = ['Violet', 'Silver', 'Blue', 'Steelblue', 'Crimson',
                               'Peru', 'Orange', 'Tan', 'Gold', 'Coral', 'Pink',
                               'Maroon', 'Green', 'Beige', 'Indigo', 'Olive',
                               'Lime', 'Cornflower Blue', 'Teal', 'Turquoise','Magenta']
            self.memory()

    def memory(self):
        
        #sets layout
        self.Layout = QGridLayout()
        self.level=self.diff

        #creating multiple counters (treis, clicked_buttons, pairs)
        self.tries_counter = 0
        self.counter_clicked = 0
        self.current_pairs = int((self.size*self.sizeb) / 2)
        
        #extending color list with itself and shuffel it
        self.color_list.extend(self.color_list)
        random.shuffle(self.color_list)
        #creating list for cord of button
        self.digits = []
        
        #creates a list for buttons
        self.buttons = []
        for i in range(self.size):
            for j in range(self.sizeb):
                
                #creates blank button
                self.button = QPushButton("")
                #connecting button to a function which a parameter 'button' is passed
                self.button.clicked.connect(lambda checked, button=self.button: self.show_color(button))
                self.buttons.append(self.button)
                #sets size for buttons
                self.button.setFixedSize(self.button_sizeb, self.button_size)
                #adds buttons
                self.Layout.addWidget(self.button,i,j)
        
        #creates Qt widget for the window
        widget = QWidget()
        widget.setLayout(self.Layout)
        self.setCentralWidget(widget)
        
        #creates widget for the amount of tries
        self.widget_1 = QLabel("Tries: 0")
        font = self.widget_1.font()
        font.setPointSize(15)
        self.widget_1.setFont(font)
        self.widget_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.widget_1,7,0)
        
        #creates widget for the amount of pairs left
        self.widget_2 = QLabel("Pairs left: %d" % self.current_pairs)
        font = self.widget_2.font()
        font.setPointSize(15)
        self.widget_2.setFont(font)
        self.widget_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.widget_2,7,2)

    #functions shows color of clicked button (2 max.)
    def show_color(self, button):
        #getting cord of clicked button
        clicked_button = self.sender()
        cords = self.buttons.index(clicked_button)
        self.digits.append(cords)

        #with the parameter button given to function, clicked button shows its color
        button.setStyleSheet(f"background-color: {self.color_list[cords]}")
        #counter of clicked buttons
        self.counter_clicked +=1
        #when counter of clicked buttons is 2
        if self.counter_clicked == 2:
            #This checks if user has clicked same button twice
            if cords == self.digits[0]:
                del self.digits[1]
                self.counter_clicked -= 1
            #When user clicked two different buttons
            else:  
                #calls check function
                b = self.check()
                #when function returns True
                if b == True:
                    #both Buttons can not be clicked again
                    for x in range(2):
                        button = self.buttons[self.digits[x]]
                        button.setEnabled(False)
                    #resetting list and counter
                    self.digits.clear()
                    self.counter_clicked = 0
                #when function returns False
                if b == False:
                    #both Buttons will no longer show its color
                    for x in range(2):
                        button = self.buttons[self.digits[x]]
                        button.setStyleSheet("background-color: none")
                    #resetting list and counter
                    self.digits.clear()
                    self.counter_clicked = 0

    #checks if both buttons have same color(TRUE) or not(FALSE)
    def check(self):
        #live counter goes one up and gets updated
        self.tries_counter += 1 
        self.widget_1.setText("Tries: %d" % self.tries_counter)

        #creating Messagebox for colors of clicked buttons
        clicked_button_color = QMessageBox()
        clicked_button_color.setWindowTitle("Colors")
        
        #when colors of button are not the same
        if self.color_list[self.digits[0]] != self.color_list[self.digits[1]]:
            #Messagebox shows following Text
            clicked_button_color.setText("1.Color: " + self.color_list[self.digits[0]] + "\n2.Color: " + self.color_list[self.digits[1]] + "\nClose one, try again!")
            clicked_button_color.exec()
            #returns False
            return False
        
        #when colors of buttons are the same color
        else:
            #live counter of pairs becomes one less and gets updated
            self.current_pairs -= 1
            self.widget_2.setText("Pairs left: %d" % self.current_pairs)

            #Messagebox shows following Text
            clicked_button_color.setText("1.Color: " + self.color_list[self.digits[0]] + "\n2.Color: " + self.color_list[self.digits[1]] + "\nGreat, you found a pair!")
            clicked_button_color.exec()

            #when all pairs are found
            if self.current_pairs == 0:
                        #Messagebox which congratulates user
                        win_window = QMessageBox()
                        win_window.setWindowTitle("Good Game!")
                        win_window.setText("You have found all pairs in " + str(self.tries_counter) + " Tries.")
                        win_window.exec()
                        #Starts a new Game
                        self.memory()
                        return None
            #returns True
            return True

    def save_score(self): #save function
        save_objects =f"{self.diff,self.tries_counter,self.current_pairs}" #creats a string which holds all necessary values
        file_name =QFileDialog.getSaveFileName(self) #get file name
        with open(file_name[0], "w+") as fobj: #write in and overwrite if saved on to again
            fobj.write(save_objects) 

    def load_game(self): #load function
        file_name =QFileDialog.getOpenFileName(self)
        with open (file_name[0], "r") as fobj:
            readIn =fobj.readline() #reads the complete line and return it as a string
        self.diff =int(readIn[1])
        self.tries_counter =int(readIn[readIn.index(",")+2]) #read in index at given postion ',+2' =5
        self.current_pairs =int(readIn[readIn.index(")")-1])

        self.widget_2 =QLabel(f"Pairs left:{self.current_pairs}")#updating the labels to the loaded in values
        self.widget_1 =QLabel(f"Tries:{self.tries_counter}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()    