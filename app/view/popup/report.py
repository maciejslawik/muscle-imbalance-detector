from tkinter import *
from app.view.popup.popup_interface import PopupInterface


class ReportPopup(PopupInterface):

    def __init__(self, report) -> None:
        self.__report = report

    def show(self) -> None:
        popup = Tk()
        popup.title('Results | Muscle imbalance detector')
        popup.geometry('550x350')
        title = Label(popup, text='Results')
        title.pack(side=TOP)
        title.config(font=('times', 12, 'bold'))
        content = Label(popup, text=self.__report)
        content.pack()
