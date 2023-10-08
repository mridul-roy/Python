import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500,height=400)

#lebel
my_level = tkinter.Label(text="Hello, I am level", font=("Arial",15))
my_level.pack()

def button_clicked():

    text = input.get()
    new_lebel = tkinter.Label(text=text,font=("Arial",12))
    new_lebel.pack()



#Button

button = tkinter.Button(text="Click Me", command=button_clicked )
button.pack()

#input

input = tkinter.Entry()
input.pack()


window.mainloop()
