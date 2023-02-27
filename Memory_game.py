'''
###########################################################
#  David Würfl  #  Piero Barboza Bidner  #  Luca Brecher  #
#  09.02.2023   #  22.02.2023            #  23.02.2023    #
#  Layout       #  Game-Function         #  SaveAndLoad   #
###########################################################
##Memory Game with PyQt6##

User can choose between 3 difficultys (Small, Medium, Big).
    -The only differenz is the number of pairs which has to be found (size of field)

Under the field, user can see a two live counters:
    -one for his tries
    -one for how many pairs are left

User can clicked a maximum of 2 Buttons, color of button is shown when clicked.
When max. of 2 Buttons where clicked, live counter of tries goes one up and a function is called which checks if both colors are the same.
    Colors are the same:
        -Buttons will always show their color
        -Buttons can not be clicked again
        -live Counter of pairs becomes one less
    
    Colors are different:
        -Button will not show its color again until it is clicked again

User has the option to save and load a game_file.
    following data is saved an loaded:
        -Counter of tries
        -Counter of pairs
        -Difficulty
    
    If game_file is loaded:
        -live counters are set to the saved value
        -found pairs are displayed on the field

Game is won, when user found all pairs.
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
        self.small_action.triggered.connect (lambda:self.set_size(1, False))
        self.size_menu.addAction(self.small_action)

        self.medium_action = QtGui.QAction("Medium", self)
        #sets field-size to medium
        self.medium_action.triggered.connect(lambda: self.set_size(2, False))
        self.size_menu.addAction(self.medium_action)

        self.big_action = QtGui.QAction("Big", self)
        #sets field-size to big
        self.big_action.triggered.connect(lambda: self.set_size(3, False))
        self.size_menu.addAction(self.big_action)

    def set_size(self, level, reset=False):
        self.diff =level
        #check if file was loaded
        if reset == True:
            self.load_data = True
        else:
            self.load_data = False
        
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
                               'Lime', 'Cornflowerblue', 'Teal', 'Turquoise','Magenta']
            self.memory()

    def memory(self):
        
        #sets layout
        self.Layout = QGridLayout()
        self.level=self.diff

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

        ############################################################
        #creating multiple counters (treis, clicked_buttons, pairs)
        self.counter_clicked = 0
        #when file is loaded
        if self.load_data != True:
            #setting counters to 0 when no data is loaded
            self.tries_counter = 0
            self.current_pairs = int((self.size*self.sizeb) / 2)
        else:
            self.load_data = False
            #get number of pair for diff which was loaded
            if self.diff == 1:
                pair = 12
            elif self.diff == 2:
                pair = 15
            elif self.diff == 3:
                pair = 21

            #color list 
            color_list = ['Violet', 'Silver', 'Blue', 'Steelblue', 'Crimson',
                               'Peru', 'Orange', 'Tan', 'Gold', 'Coral', 'Pink',
                               'Maroon', 'Green', 'Beige', 'Indigo', 'Olive',
                               'Lime', 'Cornflowerblue', 'Teal', 'Turquoise','Magenta']

            #list for indexes of buttons
            button_index = []
            #get indexes of color for buttons
            for pair in range(pair-self.current_pairs):
                color_index = [i for i, x in enumerate(self.color_list) if x == color_list[pair]]
                button_index.extend(color_index)
            #show color of buttons and buttons can not longer be clicked
            for b in range(len(button_index)):
                button = self.buttons[button_index[b]]
                button.setStyleSheet(f"background-color: {self.color_list[button_index[b]]}")
                button.setEnabled(False)
        ############################################################
        #creates Qt widget for the window
        widget = QWidget()
        widget.setLayout(self.Layout)
        self.setCentralWidget(widget)
        
        #creates widget for the amount of tries
        self.widget_1 = QLabel("Tries: %d" % self.tries_counter)
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
            readIn = fobj.readline().strip("()").split(",") #strips away the brackets and splits the string into a list with comma as a separator
        self.diff = int(readIn[0]) #read in index
        self.tries_counter = int(readIn[1]) 
        self.current_pairs = int(readIn[2])

        #set load to True when file is loaded
        load_data = True

        self.widget_2.setText(f"Pairs left: {self.current_pairs}")#updating the labels to the loaded in values
        self.widget_1.setText(f"Tries: {self.tries_counter}")
        self.set_size(self.diff, load_data) #commit to upper defined function

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()    