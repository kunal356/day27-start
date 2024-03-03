import tkinter

window = tkinter.Tk()
my_label = tkinter.Label(text="My Label", font=('Arial', 24, 'bold'))
my_label.pack(side="left", expand=True)
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.mainloop()
