from tkinter import *
from app.view.button.button_interface import ButtonInterface
from app.view.popup.about import AboutPopup


class AboutButton(ButtonInterface):

    def __init__(self) -> None:
        self.__about_popup = AboutPopup()

    def build(self) -> Button:
        return Button(None, text='About', command=self.clicked)

    def clicked(self) -> None:
        self.__about_popup.show()
