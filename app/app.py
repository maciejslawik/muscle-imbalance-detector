from tkinter import *
from PIL import Image, ImageTk
from app.view.window import Window
from app.view.button.about import AboutButton
from app.view.button.howto import HowToButton
from app.view.button.start import StartButton
from app.view.input.seconds import SecondsInput
from app.video.video_capture import VideoCapture


class App:

    def __init__(self) -> None:
        # Init main application window
        self.window = Window.build()

        # Init video capture and canvas
        self.video_capture = VideoCapture()
        self.camera_canvas = Canvas(self.window, width=self.video_capture.width, height=self.video_capture.height)
        self.camera_canvas.pack()
        self.camera_canvas.place(x=260, y=100)

        # Seconds input
        self.time_input = SecondsInput(self.window).build()
        self.time_input.pack()
        self.time_input.place(height=60, width=200, x=30, y=100)

        # Init start button
        self.start_button = StartButton(self.video_capture, self.time_input).build()
        self.start_button.master = self.window
        self.start_button.pack()
        self.start_button.place(height=60, width=200, x=30, y=160)

        # Init how-to button
        self.how_to_button = HowToButton().build()
        self.how_to_button.master = self.window
        self.how_to_button.pack()
        self.how_to_button.place(height=60, width=200, x=30, y=240)

        # Init about button
        self.about_button = AboutButton().build()
        self.about_button.master = self.window
        self.about_button.pack()
        self.about_button.place(height=60, width=200, x=30, y=520)

        # Start the app
        self.__main()
        self.window.mainloop()

    def __main(self) -> None:
        status, frame = self.video_capture.get_frame()
        if status:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.camera_canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.window.after(15, self.__main)
