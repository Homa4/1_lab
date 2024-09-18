from tkinter import *
from testFunc import hi

class MainWindow:
    def __init__(self):
        pass
        
    
    def displayMainW(self, firstW, secondW):
        # Create the main window
        root = Tk()
        root.title('Title')
        
        # Create and pack the canvas
        canvas = Canvas(root, width=500, height=500)
        canvas.pack()
        
        # Create and pack buttons
        btn1 = Button(root, text='Work1', command=firstW)
        btn2 = Button(root, text='Work2', command=secondW)
        btn1.pack()
        btn2.pack()
        
        # Start the Tkinter event loop
        root.mainloop()