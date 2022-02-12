from tkinter import *
from tkinter import ttk


def CalcPrice(*args):
    val1 = int(num1.get())
    val2 = int(num2.get())
    result.set(val1 * val2)

root = Tk()
root.title("Student Post-exams Vacation Planner")
box = ttk.Frame(root, padding = (5, 5, 100, 50)) 
num1 = IntVar()
num2 = IntVar()
result = IntVar()
ttk.Radiobutton(root, text = 'NIS', value = 1).grid(column = 0, row=3)
ttk.Radiobutton(root, text = '$', value = 2).grid(column = 0, row=4)
ttk.Radiobutton(root, text = '€', value = 3).grid(column = 0, row=5)
box.grid(column=0, row=0, rowspan = 12,sticky=(N,W,E,S))
num1_entry = ttk.Entry(box, width=50)
countrynames = ('Rome', 'London', 'Moscow', 'Berlin', 'Madrid','Paris','Washinaton')
cnames = StringVar(value=countrynames)
lbox = Listbox(box ,listvariable = cnames ,height=15, width = 15)
lbox.grid()
ttk.Label(box, text="Price: ").grid(column=4, row=1)
root.bind('<Return>', CalcPrice)
root.mainloop()