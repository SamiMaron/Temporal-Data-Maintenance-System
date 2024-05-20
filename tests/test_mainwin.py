import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
import tkinter as tk
from MainWin import MainWin
from DataBase import DataBase
from windows.SearchWin import SearchWin
from windows.GetWin import GetWin
from windows.GetHistoryWin import GetHistoryWin
from windows.UpdateWin import UpdateWin
from windows.DeleteWin import DeleteWin
from windows.SetTimeWin import SetTimeWin


@pytest.fixture
def mock_main_win():
    with patch('tkinter.Tk', new=MagicMock(spec=tk.Tk)):
        mw = MainWin()
    return mw

def test_mainwin_initialization(mock_main_win):
    mw = mock_main_win

    assert isinstance(mw._mainWin, tk.Tk)
    assert isinstance(mw._data, DataBase)
    assert isinstance(mw._today, datetime)

def test_mainwin_run(mock_main_win):
    mw = mock_main_win

    with patch.object(mw, '_build', new=MagicMock()) as mock_build:
        with patch.object(mw._mainWin, 'mainloop', new=MagicMock()) as mock_mainloop:
            mw.run()
            mock_build.assert_called_once()
            mock_mainloop.assert_called_once()

def test_mainwin_quit(mock_main_win):
    mw = mock_main_win

    with patch.object(mw._mainWin, 'destroy', new=MagicMock()) as mock_destroy:
        mw._quit()
        mock_destroy.assert_called_once()

def test_mainwin_search(mock_main_win):
    mw = mock_main_win

    with patch('windows.SearchWin.SearchWin.run', new=MagicMock()) as mock_search_run:
        mw._search()
        mock_search_run.assert_called_once()

def test_mainwin_get(mock_main_win):
    mw = mock_main_win

    with patch('windows.GetWin.GetWin.run', new=MagicMock()) as mock_get_run:
        mw._get()
        mock_get_run.assert_called_once()

def test_mainwin_get_history(mock_main_win):
    mw = mock_main_win

    with patch('windows.GetHistoryWin.GetHistoryWin.run', new=MagicMock()) as mock_get_history_run:
        mw._get_history()
        mock_get_history_run.assert_called_once()

def test_mainwin_update(mock_main_win):
    mw = mock_main_win

    with patch('windows.UpdateWin.UpdateWin.run', new=MagicMock()) as mock_update_run:
        mw._add()
        mock_update_run.assert_called_once()

def test_mainwin_delete(mock_main_win):
    mw = mock_main_win

    with patch('windows.DeleteWin.DeleteWin.run', new=MagicMock()) as mock_delete_run:
        mw._delete()
        mock_delete_run.assert_called_once()

def test_mainwin_load_input(mock_main_win):
    mw = mock_main_win

    with patch('tkinter.filedialog.askopenfilename', new=MagicMock(return_value="dummy_path.xlsx")) as mock_askopenfilename:
        with patch.object(mw._data, 'load_data', new=MagicMock()) as mock_load_data:
            mw._load_input()
            mock_askopenfilename.assert_called_once_with(filetypes=[("Excel files", ".xlsx .xls")])
            mock_load_data.assert_called_once_with("dummy_path.xlsx")

def test_mainwin_set_time(mock_main_win):
    mw = mock_main_win

    with patch('windows.SetTimeWin.SetTimeWin.run', new=MagicMock(return_value=datetime(2024, 5, 20, 12, 0))) as mock_set_time_run:
        with patch.object(mw, 'run', new=MagicMock()) as mock_run:
            mw._set_time()
            assert mw._today == datetime(2024, 5, 20, 12, 0)
            mock_run.assert_called_once()

def test_mainwin_build(mock_main_win):
    mw = mock_main_win

    with patch.object(mw, '_row0', new=MagicMock()) as mock_row0:
        with patch.object(mw, '_row5', new=MagicMock()) as mock_row5:
            mw._build()
            mw._mainWin.title.assert_called_once_with("final project med AI")
            mock_row0.assert_called_once()
            mock_row5.assert_called_once()
