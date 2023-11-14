from tkinter import *


def calculate():
    dollar_input = float(input.get())
    euro_conversion = round(dollar_input * 0.93, 2)
    number_label.config(text=f'{euro_conversion}')


window = Tk()
window.title('USD to Euro Converter')
window.config(padx=20, pady=20)

# Label
dollar_label = Label(text='USD($)', font=('Arial', 24))
dollar_label.grid(column=2, row=0)

equal_label = Label(text='is equal to', font=('Arial', 24))
equal_label.grid(column=0, row=1)

euro_label = Label(text='Euro(€)', font=('Arial', 24))
euro_label.grid(column=2, row=1)

number_label = Label(text='0', font=('Arial', 24))
number_label.grid(column=1, row=1)


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)


# Button
button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)


window.mainloop()

