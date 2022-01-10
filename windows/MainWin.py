from tkinter import *
from datetime import datetime
from windows.SearchWin import SearchWin
from windows.GetWin import GetWin
from windows.GetHistoryWin import GetHistoryWin
from windows.UpdateWin import UpdateWin
from windows.DeleteWin import DeleteWin
from tkinter import filedialog
from Uti import set_row
from windows.SetTimeWin import SetTimeWin
from DataBase import DataBase


class MainWin:

    def __init__(self):
        self._mainWin = Tk()
        self._data = DataBase()
        self._today = datetime.now()

    def run(self):
        self._build()
        self._mainWin.mainloop()

    def _search(self):
        SearchWin(self._today, self._data).run()

    def _get(self):
        GetWin(self._today, self._data).run()

    def _get_history(self):
        GetHistoryWin(self._today, self._data).run()

    def _add(self):
        UpdateWin(self._today, self._data).run()

    def _delete(self):
        DeleteWin(self._today, self._data).run()

    def _load_input(self):
        self._data.load_data(filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")]))

    def _build(self):
        self._mainWin.title("final project med AI")
        self._row0()
        self._row5()

    def _quit(self):
        self._mainWin.destroy()

    def _set_time(self):
        self._today = SetTimeWin(time=self._today).run()
        self.run()

    def _row0(self):
        arr = [
            Label(self._mainWin, text="Current Time", font=('Times', 20)),

            Label(self._mainWin, text=self._today.strftime("%d/%m/%Y %H:%M"), font=('Times', 20))
        ]
        set_row(arr, 0)

    def _row5(self):
        arr = [

            Label(self._mainWin, text=""),
            Label(self._mainWin, text=""),
            Button(self._mainWin, text="Set Time", command=self._set_time, font=('Times', 20)),
            Button(self._mainWin, text="Search", command=self._search, font=('Times', 20)),
            Button(self._mainWin, text="Get", command=self._get, font=('Times', 20)),
            Button(self._mainWin, text="Get History", command=self._get_history, font=('Times', 20)),
            Button(self._mainWin, text="Update", command=self._add, font=('Times', 20)),
            Button(self._mainWin, text="Delete", command=self._delete, font=('Times', 20)),
            Button(self._mainWin, text="Load Input", command=self._load_input, font=('Times', 20)),
            Button(self._mainWin, text="Quit", command=self._quit, font=('Times', 20))
        ]
        set_row(arr, 5)
