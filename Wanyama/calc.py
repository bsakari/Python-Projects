import tkinter

def iCalc(source, side):
    storeObj = tkinter.Frame(source, borderwidth = 4, bd = 4, bg ="powder blue")
    storeObj.pack(side = side, expand = tkinter.YES, fill = tkinter.BOTH)
    return storeObj
def button(source, side, text, command = None):
    storeObj = tkinter.Button(source, text = text, command = command)
    storeObj.pack(side = side, expand = tkinter.YES, fill = tkinter.BOTH)
    return storeObj
class app(tkinter.Frame):
    def __init__(self):
        tkinter.Frame.__init__()
        self.option_add('Font','arial 20 bold')
        self.pack(expand = tkinter.YES, fill = tkinter.BOTH)
        self.master.title('calculator')

if _name_ == '_main_':
    app().mainloop()
