# from tkinter import *
# from testFunc import hi
from mainWindow import MainWindow
from firstWindow import FirstW
from secondWindow import SecondW
mainWindow = MainWindow()
firstWindow = FirstW()
secondWindow = SecondW()
mainWindow.displayMainW(firstWindow.displayFirstW, secondWindow.displayListW)
