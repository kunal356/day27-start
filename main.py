from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def button_clicked():
    my_label["text"] = "Button got clicked"
    # my_label.config(text="Button got clicked")
    my_label.config(text=input_box.get())


# Label
my_label = Label(text="My Label", font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Button 2
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input_box = Entry(width=10)
input_box.grid(column=3, row=2)
window.mainloop()
