from tkinter import *
from app.view.popup.popup_interface import PopupInterface


class HowToPopup(PopupInterface):

    def show(self) -> None:
        popup = Tk()
        popup.title('Manual | Muscle imbalance detector')
        popup.geometry('550x350')
        title = Label(popup, text='Manual')
        title.pack(side=TOP)
        title.config(font=('times', 12, 'bold'))
        content = Label(popup, text=self.__get_manual_content())
        content.pack()

    def __get_manual_content(self) -> str:
        manual = ''
        manual += '\n1. Set the camera of your computer directly in front of the bar.\n\n'
        manual += '2. Set the movement timer in the application window. \n\n'
        manual += 'It determines how many seconds of your movement will be analysed.\n\n'
        manual += '3. Press Start. You will have 10 seconds to start the movement. Each second you will head a beep.\n\n'
        manual += '4. Start your movement when you hear a double beep.\n\n'
        manual += '5. The application will track your movement for the desired number of seconds.\n\n'
        manual += '5. You will hear a double beep when the recording finishes.\n\n'
        manual += '7. Wait for the results.\n\n'
        return manual
