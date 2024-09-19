from tkinter import *
from PIL import Image, ImageTk  # Requires: pip install pillow
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
        
        # Store image objects as instance variables to avoid garbage collection
        self.bg_photo = None

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
        # Define window title and size
        self._mainWin.title("Final Project Med AI")
        self._mainWin.geometry("800x600")  # Adjust window size here

        # Load and set background image
        bg_image = Image.open("background.jpg")  # Replace with a valid image path
        bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  # Resize background to fit the window
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self._mainWin, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window

        self._row0()  # Display current time at the top
        self._row5()  # Buttons below the time

    def _quit(self):
        self._mainWin.destroy()

    def _set_time(self):
        self._today = SetTimeWin(time=self._today).run()
        self.run()

    def _row0(self):
        """ Display the current time in the center of the window, above the buttons """
        time_label = Label(self._mainWin, text=self._today.strftime("%d/%m/%Y %H:%M"), font=('Arial', 24), bg="#f0f0f0", fg="#333")
        time_label.place(relx=0.5, rely=0.2, anchor=CENTER)  # Centered in the middle, with some space above the buttons

    def _row5(self):
        """ Display buttons in a single row """
        button_frame = Frame(self._mainWin, bg="#f0f0f0")
        button_frame.place(relx=0.5, rely=0.6, anchor=CENTER)  # Center the buttons in the window

        buttons = [
            Button(button_frame, text="Set Time", command=self._set_time, font=('Arial', 15), bg="#4CAF50", fg="white"),
            Button(button_frame, text="Search", command=self._search, font=('Arial', 15), bg="#2196F3", fg="white"),
            Button(button_frame, text="Get", command=self._get, font=('Arial', 15), bg="#FFC107", fg="black"),
            Button(button_frame, text="Get History", command=self._get_history, font=('Arial', 15), bg="#9C27B0", fg="white"),
            Button(button_frame, text="Update", command=self._add, font=('Arial', 15), bg="#FF5722", fg="white"),
            Button(button_frame, text="Delete", command=self._delete, font=('Arial', 15), bg="#F44336", fg="white"),
            Button(button_frame, text="Load Input", command=self._load_input, font=('Arial', 15), bg="#3F51B5", fg="white"),
            Button(button_frame, text="Quit", command=self._quit, font=('Arial', 15), bg="#9E9E9E", fg="white")
        ]

        for i, button in enumerate(buttons):
            button.grid(row=0, column=i, padx=5, pady=5)  # Place all buttons in the same row (row=0)
