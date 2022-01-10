from tkinter import *
from datetime import datetime
from Uti import set_row
from Uti import check_entery
from windows.TextMessage import TextMessage


class UpdateWin:
    def __init__(self, recivedtime, data):
        self._win = Toplevel()
        self._first_name_label = Label(self._win, text="First Name:")
        self._first_name = Entry(self._win, width=50, borderwidth=5, )
        self._last_name_label = Label(self._win, text="Last Name:")
        self._last_name = Entry(self._win, width=50, borderwidth=5, )
        self._lonic_label = Label(self._win, text="Lonic Name or Num:")
        self._lonic = Entry(self._win, width=50, borderwidth=5, )
        self._date = Entry(self._win, width=50, borderwidth=5, )
        self._time = recivedtime
        self._year_label = Label(self._win, text="Year:")
        self._year = Entry(self._win, width=50, borderwidth=5, )
        self._month_label = Label(self._win, text="Month:")
        self._month = Entry(self._win, width=50, borderwidth=5, )
        self._day_label = Label(self._win, text="Day:")
        self._day = Entry(self._win, width=50, borderwidth=5, )
        self._hour_label = Label(self._win, text="Hour:")
        self._hour = Entry(self._win, width=50, borderwidth=5, )
        self._min_label = Label(self._win, text="Min:")
        self._min = Entry(self._win, width=50, borderwidth=5, )
        self._new_val_label = Label(self._win, text="New Value:")
        self._new_val = Entry(self._win, width=50, borderwidth=5, )
        self._data = data

    def run(self):
        self._win.title("Search Window")
        self._build()
        self._win.mainloop()

    def _build(self):
        self._row0()
        self._row1()
        self._row2()
        self._row3()
        self._row4()
        self._row5()
        self._row6()
        self._row7()
        self._row8()
        self._row10()

    def _row0(self):
        arr = [
            self._first_name_label,
            self._first_name
        ]
        set_row(arr, 0)

    def _row1(self):
        arr = [
            self._last_name_label,
            self._last_name
        ]
        set_row(arr, 1)

    def _row2(self):
        arr = [
            self._lonic_label,
            self._lonic
        ]
        set_row(arr, 2)

    def _row3(self):
        arr = [
            self._year_label,
            self._year
        ]
        set_row(arr, 3)

    def _row4(self):
        arr = [
            self._month_label,
            self._month
        ]
        set_row(arr, 4)

    def _row5(self):
        arr = [
            self._day_label,
            self._day
        ]
        set_row(arr, 5)

    def _row6(self):
        arr = [
            self._hour_label,
            self._hour
        ]
        set_row(arr, 6)

    def _row7(self):
        arr = [
            self._min_label,
            self._min
        ]
        set_row(arr, 7)

    def _row8(self):
        arr = [
            self._new_val_label,
            self._new_val
        ]
        set_row(arr, 8)

    def _row10(self):
        arr = [
            Label(self._win, text=""),
            Label(self._win, text=""),
            Button(self._win, text="Update", command=self.__update),
            Button(self._win, text="Quit", command=self._quit)
        ]
        set_row(arr, 10)

    def __update(self):
        if self.__check_valid():
            if self._data.update_data(self._first_name.get(), self._last_name.get(), self._lonic.get(),
                                      f"{self._day.get()}/{self._month.get()}/{self._year.get()}",
                                      f"{self._hour.get()}:{self._min.get()}", self._new_val.get(),
                                      self._time.strftime("%Y/%m/%d %H:%M")):
                TextMessage("data was updated").run()
            else:
                TextMessage("data update failed").run()

    def __check_valid(self):
        is_valid = True
        if not check_entery(self._first_name_label, self._first_name):
            is_valid = False
        if not check_entery(self._last_name_label, self._last_name):
            is_valid = False
        if not check_entery(self._lonic_label, self._lonic):
            is_valid = False
        if not check_entery(self._year_label, self._year):
            is_valid = False
        if not check_entery(self._month_label, self._month):
            is_valid = False
        if not check_entery(self._day_label, self._day):
            is_valid = False
        if not check_entery(self._new_val_label, self._new_val):
            is_valid = False
        return is_valid

    def _quit(self):
        self._win.destroy()
        self._win.quit()
