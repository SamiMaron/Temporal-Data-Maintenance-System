from tkinter import *
from Uti import set_row


class TextMessage:

    def __init__(self, text):
        self._win = Toplevel()
        self.text = text

    def run(self):
        self._win.title("Message")
        self._build()
        self._win.mainloop()

    def _build(self):
        self._row0()
        self._row5()

    def _row0(self):
        arr = [Label(self._win, text=self.text)
               ]
        set_row(arr, 0)

    def _row5(self):
        arr = [

            Button(self._win, text="quit", command=self._quit)
        ]
        set_row(arr, 5)

    def _quit(self):
        self._win.destroy()
        self._win.quit()
