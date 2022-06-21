from tkinter import *

def createAdminAccount():
        return

def first_window():
    window = Tk()

    window['width'] = 1080
    window['height'] = 720

    #b_width = window.cget('width') * 0.1
    #b_height = window.cget('height') * 0.1
    button_creation = Button(window, text="Create Admin account", activebackground="blue", command=createAdminAccount)

    button_creation.place(x=0,y=0)
    return window