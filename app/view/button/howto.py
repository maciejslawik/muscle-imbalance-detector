from tkinter import *
from app.view.button.button_interface import ButtonInterface
from app.view.popup.howto import HowToPopup


class HowToButton(ButtonInterface):

    def __init__(self) -> None:
        self.__how_to_popup = HowToPopup()

    def build(self) -> Button:
        return Button(None, text='How to', command=self.clicked)

    def clicked(self) -> None:
        self.__how_to_popup.show()
