from abc import abstractmethod
from tkinter import *


class ButtonInterface:

    @abstractmethod
    def build(self) -> Button:
        pass
