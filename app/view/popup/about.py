from tkinter import *
from app.view.popup.popup_interface import PopupInterface


class AboutPopup(PopupInterface):

    def show(self) -> None:
        popup = Tk()
        popup.title('About | Muscle imbalance detector')
        popup.geometry('400x150')
        title = Label(popup, text='About')
        title.pack(side=TOP)
        title.config(font=('times', 12, 'bold'))
        content = Label(popup, text='\nVersion 0.1.0-alpha\nMaciej Sławik\n2019\n')
        content.pack()
