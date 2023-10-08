from tkinter import *


def calculate_to_Km():
    miles = float(mails_input.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=80, pady=40)

mails_input = Entry(width=9)
mails_input.grid(column=1, row=0)

miles_label = Label(text="Mails")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_leval = Label(text="Km")
km_leval.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_to_Km)
calculate_button.grid(column=1, row=2)

window.mainloop()
