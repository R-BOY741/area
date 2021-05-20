from tkinter import *
root=Tk()
root.title("OOP using tkinter")
root.geometry("380x360")

class Circle:
    myresult = StringVar()
    def __init__(self, window):
        self.lblradius=Label(window, text="please enter the radius")
        self.lblradius.pack()
        self.txtrad = Entry(window)
        self.txtrad.pack()
        self.btncalc = Button(window, text="calculate area", borderwidth="10")
        self.btncalc.pack()
        self.lblradius=Label(window, text="", textvariable=self.myresult)
        self.lblradius.pack()

    def area(self):
        radius = int(self.txtrad.get())
        answer = 3.4*(radius**2)
        self.myresult.set("The area is" + str ( answer))


obj_circle=Circle(root)

root.mainloop()
