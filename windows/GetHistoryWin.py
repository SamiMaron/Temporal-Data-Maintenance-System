from tkinter import *
from datetime import datetime
from Uti import set_row
from Uti import check_entery
from windows.InfoTable import InfoTable


class GetHistoryWin:
    def __init__(self, recivedtime, data):
        self._win = Toplevel()
        self._first_name_label = Label(self._win, text="First Name:")
        self._first_name = Entry(self._win, width=50, borderwidth=5, )
        self._last_name_label = Label(self._win, text="Last Name:")
        self._last_name = Entry(self._win, width=50, borderwidth=5, )
        self._lonic_label = Label(self._win, text="Lonic Name or Num:")
        self._lonic = Entry(self._win, width=50, borderwidth=5, )
        self._from_year_label = Label(self._win, text="From Year:")
        self._from_year = Entry(self._win, width=50, borderwidth=5, )
        self._to_year_label = Label(self._win, text="To Year:")
        self._to_year = Entry(self._win, width=50, borderwidth=5, )
        self._from_month_label = Label(self._win, text="From Month:")
        self._from_month = Entry(self._win, width=50, borderwidth=5, )
        self._to_month_label = Label(self._win, text="To Month:")
        self._to_month = Entry(self._win, width=50, borderwidth=5, )
        self._from_day_label = Label(self._win, text="From Day:")
        self._from_day = Entry(self._win, width=50, borderwidth=5, )
        self._to_day_label = Label(self._win, text="To Day:")
        self._to_day = Entry(self._win, width=50, borderwidth=5, )
        self._from_hour_label = Label(self._win, text="From Hour:")
        self._from_hour = Entry(self._win, width=50, borderwidth=5, )
        self._to_hour_label = Label(self._win, text="To Hour:")
        self._to_hour = Entry(self._win, width=50, borderwidth=5, )
        self._from_min_label = Label(self._win, text="From Min:")
        self._from_min = Entry(self._win, width=50, borderwidth=5, )
        self._to_min_label = Label(self._win, text="To Min:")
        self._to_min = Entry(self._win, width=50, borderwidth=5, )
        self._time = recivedtime
        self._data = data

    def run(self):
        self._win.title("Search Window")
        self._build()
        self._win.mainloop()

    def _build(self):
        self._row0()
        self._row1()
        self._row2()
        self._row4()
        self._row5()
        self._row6()
        self._row7()
        self._row8()

    def _row0(self):
        arr = [
            self._first_name_label,
            self._first_name

        ]
        set_row(arr, 0)

    def _row1(self):
        arr = [
            self._last_name_label,
            self._last_name,

        ]
        set_row(arr, 1)

    def _row2(self):
        arr = [
            self._lonic_label,
            self._lonic,

        ]
        set_row(arr, 2)

    def _row4(self):
        arr = [
            self._from_year_label,
            self._from_year,
            self._to_year_label,
            self._to_year
        ]
        set_row(arr, 4)

    def _row5(self):
        arr = [
            self._from_month_label,
            self._from_month,
            self._to_month_label,
            self._to_month
        ]
        set_row(arr, 5)

    def _row6(self):
        arr = [
            self._from_day_label,
            self._from_day,
            self._to_day_label,
            self._to_day
        ]
        set_row(arr, 6)

    def _row7(self):
        arr = [
            self._from_hour_label,
            self._from_hour,
            self._to_hour_label,
            self._to_hour
        ]
        set_row(arr, 7)

    def _row8(self):
        arr = [
            self._from_min_label,
            self._from_min,
            self._to_min_label,
            self._to_min
        ]
        set_row(arr, 8)

        self.button = Button(self._win, text="Search", command=self._get_history)
        self.button.grid(row=15, column=7)

        self.button = Button(self._win, text="Quit", command=self._quit)
        self.button.grid(row=15, column=8)

    def _get_history(self):
        if self.__check_valid():
            InfoTable(self._data.get_history(self._first_name.get(), self._last_name.get(), self._lonic.get(),
                                             f"{self._from_day.get()}-{self._from_month.get()}-{self._from_year.get()}",
                                             f"{self._from_hour.get()}:{self._from_min.get()}",
                                             f"{self._to_day.get()}-{self._to_month.get()}-{self._to_year.get()}",
                                             f"{self._to_hour.get()}:{self._to_min.get()}",
                                             self._time.strftime("%Y/%m/%d %H:%M"))).run()

    def __check_valid(self):
        is_valid = True
        if not check_entery(self._first_name_label, self._first_name):
            is_valid = False
        if not check_entery(self._last_name_label, self._last_name):
            is_valid = False
        if not check_entery(self._lonic_label, self._lonic):
            is_valid = False
        return is_valid

    def _quit(self):
        self._win.destroy()
        self._win.quit()
