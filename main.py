from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="My Label", font=('Arial', 24, 'bold'))
my_label.pack()


def button_clicked():
    my_label["text"] = "Button got clicked"
    # my_label.config(text="Button got clicked")
    my_label.config(text=input_box.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

input_box = Entry(width=10)
input_box.pack()
window.mainloop()
