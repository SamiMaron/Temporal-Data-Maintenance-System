from tkinter import *
from Uti import set_row
from windows.InfoTable import InfoTable
from DataBase import DataBase


class SearchWin:
    def __init__(self, received_time, data):
        self._win = Toplevel()
        self._first_name = Entry(self._win, width=50, borderwidth=5, )
        self._last_name = Entry(self._win, width=50, borderwidth=5, )
        self._lonic = Entry(self._win, width=50, borderwidth=5, )
        self._time = received_time
        self._data = data

    def run(self):
        self._win.title("search window")
        self._build()
        self._win.mainloop()

    def _build(self):
        self._row0()
        self._row1()
        self._row3()
        self._row5()

    def _row0(self):
        arr = [
            Label(self._win, text="Set First Name:"),
            self._first_name
        ]
        set_row(arr, 0)

    def _row1(self):
        arr = [
            Label(self._win, text="Set Last Name:"),
            self._last_name
        ]
        set_row(arr, 1)

    def _row3(self):
        arr = [
            Label(self._win, text="Lonic Name or Num:"),
            self._lonic
        ]
        set_row(arr, 3)

    def _row5(self):
        arr = [
            Label(self._win, text=""),
            Label(self._win, text=""),
            Button(self._win, text="Search", command=self._active),
            Button(self._win, text="Quit", command=self._quit)
        ]
        set_row(arr, 5)

    def _active(self):
        if self._first_name != '':
            InfoTable(self._data.search_info(self._first_name.get(), self._last_name.get(), self._lonic.get(),
                                             self._time.strftime("%Y/%m/%d %H:%M"))).run()
        print("searching pressed", self._time)

    def _quit(self):
        self._win.destroy()
        self._win.quit()
