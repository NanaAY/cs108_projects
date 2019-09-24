'''Graphical User Interface for the Temperature Converter Program
Created Spring 2018
homework11
@author: Nana Osei Asiedu Yirenkyi (na29) 
'''

from tkinter import *
from temperature import *


class Gui:
    '''Gui Class'''
    def __init__(self, window):
        '''constructor that receives a window object from its calling program
         and then creates and places widgets on that window '''
        self._temp = Temperature()
        self._input1 = StringVar()
        self._celsius = StringVar()
        self._message = StringVar()
        self._message.set('Welcome!')
        
        temp_label = Label(window, text= 'Temperature(in Fahrenheit):')
        temp_label.grid(row=0, column=0, sticky=E)
        
        celsius_label = Label(window, textvariable= self._celsius)
        celsius_label.grid(row=1, column=1, sticky=W)
        
        message_label = Label(window, textvariable= self._message)
        message_label.grid(row=2, column=0, sticky=E)
        
        input1_entry = Entry(window, width=5, textvariable= self._input1)
        input1_entry.grid(row=0, column=1, sticky=W)
        
        convert_button = Button(window, text='Convert to celsius', command=self.convert_temp)
        convert_button.grid(row=1,column=0, sticky=E)
        
        
    def convert_temp(self):
        try:
            if (self._input1.get().isalpha() == False) and (float(self._input1.get()) > -459.67):
                celsius = self._temp.get_temp_celsius(self._input1.get())
                self._celsius.set(celsius)
            else:
                raise ValueError
        except ValueError:
            self._message.set('Invalid Value.')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#                DRIVER  SCRIPT
if __name__ == '__main__':
    root = Tk()
    root.title('Calculator')
    app = Gui(root)
    root.mainloop()