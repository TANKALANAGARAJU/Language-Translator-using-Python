from tkinter import *
from googletrans import LANGUAGES, Translator

# Get a list of all supported languages
all_languages = list(LANGUAGES.values())

window = Tk()
window.title("vishnu's  language Translator")

# Styling
window.geometry("500x300")
window.configure(bg='#f0f0f0')

mainframe = Frame(window, bg='#f0f0f0')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

lan1 = StringVar(window)
lan2 = StringVar(window)


def trans():
    translator = Translator()
    translation = translator.translate(var.get(), src=lan1.get(), dest=lan2.get())
    var1.set(translation.text)


lan1menu = OptionMenu(mainframe, lan1, *all_languages)
lan1menu.config(width=20)
Label(mainframe, text="Select source language", bg='#f0f0f0').grid(row=0, column=1, pady=(10, 0))
lan1menu.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

lan2menu = OptionMenu(mainframe, lan2, *all_languages)
lan2menu.config(width=20)
Label(mainframe, text="Select target language", bg='#f0f0f0').grid(row=0, column=2, pady=(10, 0))
lan2menu.grid(row=1, column=2, pady=(0, 10))

Label(mainframe, text="Enter text ", bg='#f0f0f0').grid(row=2, column=0, pady=(10, 0))
var = StringVar()
textbox = Entry(mainframe, textvariable=var, width=40).grid(row=2, column=1, pady=(10, 0))

Label(mainframe, text="Output", bg='#f0f0f0').grid(row=2, column=2, pady=(10, 0))
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1, width=40).grid(row=2, column=3, pady=(10, 0))

button = Button(mainframe, text='Translate', command=trans, bg='#4caf50', fg='white', font=('Arial', 12)).grid(row=3, column=1, columnspan=3, pady=(10, 0))

window.mainloop()
