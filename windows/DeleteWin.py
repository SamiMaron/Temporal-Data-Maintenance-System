from tkinter import *
from Uti import set_row
from Uti import check_entery
from windows.TextMessage import TextMessage


class DeleteWin:
    def __init__(self, recivedtime, data):
        self.__win = Toplevel()
        self.__first_name_label = Label(self.__win, text="First Name:")
        self.__first_name = Entry(self.__win, width=50, borderwidth=5, )
        self.__last_name_label = Label(self.__win, text="Last Name:")
        self.__last_name = Entry(self.__win, width=50, borderwidth=5, )
        self.__lonic_label = Label(self.__win, text="Lonic Name or Num:")
        self.__lonic = Entry(self.__win, width=50, borderwidth=5, )
        self.__date = Entry(self.__win, width=50, borderwidth=5, )
        self.__time = recivedtime
        self.__year_label = Label(self.__win, text="Year:")
        self.__year = Entry(self.__win, width=50, borderwidth=5, )
        self.__month_label = Label(self.__win, text="Month:")
        self.__month = Entry(self.__win, width=50, borderwidth=5, )
        self.__day_label = Label(self.__win, text="Day:")
        self.__day = Entry(self.__win, width=50, borderwidth=5, )
        self.__hour_label = Label(self.__win, text="Hour:")
        self.__hour = Entry(self.__win, width=50, borderwidth=5, )
        self.__min_label = Label(self.__win, text="Min:")
        self.__min = Entry(self.__win, width=50, borderwidth=5, )
        self.__data = data

    def run(self):
        self.__win.title("search window")
        self.__build()
        self.__win.mainloop()

    def __build(self):
        self.__row0()
        self.__row1()
        self.__row2()
        self.__row3()
        self.__row4()
        self.__row5()
        self.__row6()
        self.__row7()

    def __row0(self):
        arr = [
            self.__first_name_label,
            self.__first_name
        ]
        set_row(arr, 0)

    def __row1(self):
        arr = [
            self.__last_name_label,
            self.__last_name
        ]
        set_row(arr, 1)

    def __row2(self):
        arr = [
            self.__lonic_label,
            self.__lonic
        ]
        set_row(arr, 2)

    def __row3(self):
        arr = [
            self.__year_label,
            self.__year
        ]
        set_row(arr, 3)

    def __row4(self):
        arr = [
            self.__month_label,
            self.__month
        ]
        set_row(arr, 4)

    def __row5(self):
        arr = [
            self.__day_label,
            self.__day
        ]
        set_row(arr, 5)

    def __row6(self):
        arr = [
            self.__hour_label,
            self.__hour
        ]
        set_row(arr, 6)

    def __row7(self):
        arr = [
            self.__min_label,
            self.__min
        ]
        set_row(arr, 7)

        self.button = Button(self.__win, text="Delete", command=self.__delete)
        self.button.grid(row=8, column=7)

        self.button = Button(self.__win, text="Quit", command=self.__quit)
        self.button.grid(row=8, column=8)

    def __delete(self):
        if self.__check_valid():
            if self.__data.delete_data(self.__first_name.get(), self.__last_name.get(), self.__lonic.get(),
                                       f"{self.__day.get()}-{self.__month.get()}-{self.__year.get()}",
                                       f"{self.__hour.get()}:{self.__min.get()}",
                                       self.__time.strftime("%Y-%m-%d %H:%M")):
                TextMessage("Delete success").run()
            else:
                TextMessage("Delete failed").run()

    def __check_valid(self):
        is_valid = True
        if not check_entery(self.__first_name_label, self.__first_name):
            is_valid = False
        if not check_entery(self.__last_name_label, self.__last_name):
            is_valid = False
        if not check_entery(self.__lonic_label, self.__lonic):
            is_valid = False
        if not check_entery(self.__year_label, self.__year):
            is_valid = False
        if not check_entery(self.__month_label, self.__month):
            is_valid = False
        if not check_entery(self.__day_label, self.__day):
            is_valid = False
        return is_valid

    def __quit(self):
        self.__win.destroy()
        self.__win.quit()
