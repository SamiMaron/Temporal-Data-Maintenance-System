from datetime import datetime
from tkinter import *
from Uti import set_row


class SetTimeWin:
    def __init__(self, time):
        self._win = Toplevel()
        self._year = Entry(self._win, width=50, borderwidth=5,)
        self._month = Entry(self._win, width=50, borderwidth=5)
        self._day = Entry(self._win, width=50, borderwidth=5)
        self._hour = Entry(self._win, width=50, borderwidth=5)
        self._min = Entry(self._win, width=50, borderwidth=5)
        self._yearInt = int(time.strftime("%Y"))
        self._monthInt = int(time.strftime("%m"))
        self._dayInt = int(time.strftime("%d"))
        self._hourInt = int(time.strftime("%H"))
        self._minInt = int(time.strftime("%M"))
        self._time = time

    def build(self):
        self._win.title("Set time")
        self._year.insert(END, self._yearInt)
        self._month.insert(END, self._monthInt)
        self._day.insert(END, self._dayInt)
        self._hour.insert(END, self._hourInt)
        self._min.insert(END, self._minInt)
        self._row0()
        self._row1()
        self._row2()
        self._row3()
        self._row4()
        self._row5()

    def _row0(self):
        arr = [
            Label(self._win, text="Set Year:"),
            self._year
        ]
        set_row(arr, 0)

    def _row1(self):
        arr = [
            Label(self._win, text="Set Month:"),
            self._month
        ]
        set_row(arr, 1)

    def _row2(self):
        arr = [
            Label(self._win, text="Set Day:"),
            self._day
        ]
        set_row(arr, 2)

    def _row3(self):
        arr = [
            Label(self._win, text="Set Hour:"),
            self._hour
        ]
        set_row(arr, 3)

    def _row4(self):
        arr = [
            Label(self._win, text="Min"),
            self._min
        ]
        set_row(arr, 4)

    def _row5(self):
        arr = [
            Button(self._win, text="Set Time", command=self._set_time),
            Button(self._win, text="now", command=self.__fill_now)
        ]
        set_row(arr, 5)

    def _set_time(self):
        self._yearInt = int(self._year.get())
        self._monthInt = int(self._month.get())
        self._dayInt = int(self._day.get())
        self._hourInt = int(self._hour.get())
        self._minInt = int(self._min.get())
        self._win.destroy()
        self._win.quit()

    def __fill_now(self):
        self._year.delete(0, END)
        self._month.delete(0, END)
        self._day.delete(0, END)
        self._hour.delete(0, END)
        self._min.delete(0, END)
        self._year.insert(END, datetime.now().strftime("%Y"))
        self._month.insert(END, datetime.now().strftime("%m"))
        self._day.insert(END, datetime.now().strftime("%d"))
        self._hour.insert(END, datetime.now().strftime("%H"))
        self._min.insert(END, datetime.now().strftime("%M"))

    def run(self):
        self.build()
        self._win.mainloop()
        try:
            return datetime(
                day=self._dayInt,
                minute=self._minInt,
                year=self._yearInt,
                hour=self._hourInt,
                month=self._monthInt
            )
        except ValueError:
            return self._time
