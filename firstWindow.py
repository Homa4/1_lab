from tkinter import *
from testFunc import hi

class FirstW:
    def __init__(self):
        pass
        
    def displayFirstW(self):
        root = Tk()
        root.title('Title')
        canvas = Canvas(root, width=500, height=500)
        canvas.pack()
        btn1 = Button(root, text='Next', command=self.displayNextWindow)
        btn2 = Button(root, text='Quit', command=root.destroy)
        btn1.pack()
        btn2.pack()
        root.mainloop()

    def displayNextWindow(self):
        root = Tk()
        root.title('Title')
        canvas = Canvas(root, width=500, height=500)
        canvas.pack()
        
        btn1 = Button(root, text='Back', command=root.destroy)
        btn2 = Button(root, text='Yes', command=hi)
        btn3 = Button(root, text='Cancel', command=root.destroy)
        btn1.pack()
        btn2.pack()
        btn3.pack()
        
        
        root.mainloop()
