from tkinter import *
from app.view.input.input_interface import  InputInterface


class SecondsInput(InputInterface):

    __default_movement_time = '3'

    def __init__(self, window) -> None:
        self.window = window

    def build(self) -> Frame:
        frame = Frame(self.window)

        label_text = StringVar()
        label_text.set('Movement time (s) ')
        label = Label(frame, textvariable=label_text, height=4)
        label.pack(side='left')

        vcmd = (self.window.register(self.__validate))
        entry = Entry(frame, validate='key', validatecommand=(vcmd, '%P'), bd=5)
        entry.pack(side='left')
        entry.insert(0, self.__default_movement_time)

        frame.label = label
        frame.input = entry
        return frame

    def __validate(self, character) -> bool:
        if str.isdigit(character) or character == '':
            return True
        else:
            return False
