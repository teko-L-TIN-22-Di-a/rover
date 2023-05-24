from tkinter import Button, Label, Entry, Listbox, Toplevel
from Resources.Windows import centerd_window

class widgets:
    def __init__(self,__master, __text, __anchor, __xvalue, __yvalue):
        self.master = __master
        self.text = __text
        self.anchor = __anchor
        self.xvalue = __xvalue
        self.yvalue = __yvalue
        self.output =''

    def label(self):
        label = Label(self.master, text = self.text, justify = 'left')
        label.place(anchor = self.anchor, x = self.xvalue, y = self.yvalue)

    def button(self, command):
        button = Button(self.master, text = self.text, command = command)
        button.place(anchor = self.anchor, x = self.xvalue, y = self.yvalue)

    def sizedbutton(self, command, width):
        button = Button(self.master, text = self.text, command = command, width = width)
        button.place(anchor = self.anchor, x = self.xvalue, y = self.yvalue)

    def entry(self):
        label = Label(self.master, text = self.text)
        label.place(anchor = self.anchor, x = self.xvalue, y = self.yvalue -30)
        widget = Entry(self.master, justify = 'center', validate = 'key')
        widget.place(anchor = self.anchor, x = self.xvalue, y = self.yvalue)
        widget.configure(validate='key')
        command = widget.register(self.validation)
        widget.configure(validatecommand= (command, '%S', '%P'))

    def validation(self, char, value):
        if len(value) > 15:
            print('> entry at its limit')
            return False
        elif char == ' ':
            return True
        elif not char.isalpha():
            return False
        else:
            return True

    def on_select(self, event):
        try:
            index = self.lb.curselection()[0]
            self.output = self.lb.get(index)
            if labl:
                labl.configure(text = self.output)
                dist = self.lb.winfo_height()
                labl.place(anchor = self.anchor, x = self.xvalue, y = self.yvalue + dist)
        except IndexError:
            return
        except NameError:
            return

    def listbox(self, selection, height_value, output):
        if height_value == 0:
            height_value = len(selection)
        label = Label(self.master, text = self.text)
        label.place(anchor = self.anchor, x = self.xvalue, y = self.yvalue -30)
        self.lb = Listbox(self.master, height = height_value, justify = 'center')
        self.lb.place(anchor = self.anchor, x = self.xvalue, y =  self.yvalue)
        for select in selection:
            self.lb.insert('end', select)
        self.lb.bind("<<ListboxSelect>>", self.on_select)
        if output == 'y':
            global labl
            labl = Label(self.master, text = self.output)

def widgets_remove(window):
        try:
            for widgets in window.winfo_children():
                widgets.place_forget()
        except AttributeError:
            print('>--widgets remove error--all fine--<')

def widgets_infowindow(name, infotext):
    widgets_infowindow = centerd_window(name, 200,100)
    widgets_infowindow_label = Label(widgets_infowindow, text = infotext)
    widgets_infowindow_label.pack(side = 'top', padx = 5, pady = 5)
    label_width = widgets_infowindow_label.winfo_width()
    label_height = widgets_infowindow_label.winfo_height()
    if label_width > 200:
        widgets_infowindow.geometry(f'{label_width}x100')
        if label_height > 100:
            widgets_infowindow.geometry(f'{label_width}x{label_height}')
    elif label_height > 100:
        widgets_infowindow.geometry(f'200x{label_height}')
    okbutton = Button(widgets_infowindow, text = 'ok', command = widgets_infowindow.destroy)
    okbutton.pack(side = 'bottom', padx = 5, pady = 5)