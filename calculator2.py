from tkinter import*

def icalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder yellow")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button (source, side, text, comand=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def__init__(self):
    self.option_add('*Front', 'arial 20 bold')
    self.pack(expand=YES, fill=BOTH)
    self.master.title('my calculator')