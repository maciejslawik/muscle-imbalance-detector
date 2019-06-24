from tkinter import *


class Window:

    @staticmethod
    def build() -> Tk:
        window = Tk()
        window.title('Muscle imbalance detector')
        window.geometry('930x610')

        title = Label(window, text='\nMUSCLE IMBALANCE DETECTOR')
        title.pack(side=TOP)
        title.config(font=('times', 18, 'bold'))

        footer = Label(window, text='Created by Maciej Sławik, 2019')
        footer.pack(side=BOTTOM)

        return window
