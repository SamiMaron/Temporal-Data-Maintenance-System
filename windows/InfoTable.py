from tkinter import *
from tkinter import ttk
from Uti import set_row


class InfoTable:
    def __init__(self, data):
        self._win = Toplevel()
        self._data = data

    def run(self):
        self._win.title("info window")
        if self._data.empty:
            self._build_empty()
        else:
            self._build()
            self._win.mainloop()

    def _build_empty(self):
        Label(self._win, text='info no found').grid(row=0, column=0)

    def _build(self):
        self._win.geometry("1100x500")
        main_frame = Frame(self._win)
        main_frame.pack(fill=BOTH, expand=1)
        canvas = Canvas(main_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        content = Frame(canvas)
        canvas.create_window((0, 0), window=content, anchor="nw")
        self._row0(content)
        self._build_content(content)

    def _row0(self, filler):
        arr = [
            Label(filler, text='First name'),
            ttk.Separator(filler, orient='vertical'),
            Label(filler, text='Last name'),
            ttk.Separator(filler, orient='vertical'),
            Label(filler, text='LOINC-NUM'),
            ttk.Separator(filler, orient='vertical'),
            Label(filler, text='LOINC-NAME'),
            ttk.Separator(filler, orient='vertical'),
            Label(filler, text='Value'),
            ttk.Separator(filler, orient='vertical'),
            Label(filler, text='Unit'),
            ttk.Separator(filler, orient='vertical'),
            Label(filler, text='Valid start time'),
            ttk.Separator(filler, orient='vertical'),
            Label(filler, text='Transaction time'),
            ttk.Separator(filler, orient='vertical'),
            Label(filler, text='Valid stop time'),
        ]
        set_row(arr, 0)

    def _build_content(self, filler):
        for i, row in self._data.iterrows():
            arr = [
                Label(filler, text=row['First name']),
                ttk.Separator(filler, orient='vertical'),
                Label(filler, text=row['Last name']),
                ttk.Separator(filler, orient='vertical'),
                Label(filler, text=row['LOINC-NUM']),
                ttk.Separator(filler, orient='vertical'),
                Label(filler, text=row['LONG COMMON NAME']),
                ttk.Separator(filler, orient='vertical'),
                Label(filler, text=row['Value']),
                ttk.Separator(filler, orient='vertical'),
                Label(filler, text=row['Unit']),
                ttk.Separator(filler, orient='vertical'),
                Label(filler, text=row['Valid start time']),
                ttk.Separator(filler, orient='vertical'),
                Label(filler, text=row['Transaction time']),
                ttk.Separator(filler, orient='vertical'),
                Label(filler, text=row['Valid stop time'])
            ]
            set_row(arr, i + 1)

    def _quit(self):
        self._win.destroy()
        self._win.quit()
