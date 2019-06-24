from abc import abstractmethod
from tkinter import *


class InputInterface:

    @abstractmethod
    def build(self) -> Frame:
        pass
