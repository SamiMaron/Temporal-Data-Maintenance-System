from tkinter import ttk


def set_row(arr, row):
    col = 0
    for i in arr:
        if type(i) == type(ttk.Separator()):
            i.grid(row=row, column=col,  sticky="ns")
        else:
            i.grid(row=row, column=col)
        col += 1


def check_entery(label, entry):
    if entry.get() == "":
        label.config(fg="red")
        return False
    else:
        label.config(fg="black")
        return True
