import cv2
import time
import sys
from threading import Thread
from app.filesystem.snapshot_storage import SnapshotStorage


class VideoCapture:
    __snapshot_frequency = 0.3
    __delay = 10

    def __init__(self) -> None:
        self.__video = cv2.VideoCapture(0)
        self.__video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.__video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self.width = self.__video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.__video.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.__video_thread = Thread(target=self.__update, args=())
        self.__video_thread.daemon = True
        self.__video_thread.start()
        self.status = False
        self.frame = None
        self.__recording_thread = None

    def __del__(self) -> None:
        if self.__video.isOpened():
            self.__video.release()

    def get_frame(self) -> tuple:
        return self.status, self.frame

    def record(self, movement_time) -> None:
        def __process_recording():
            movement_finished = False
            while not movement_finished:
                try:
                    number_of_frames = round(movement_time / self.__snapshot_frequency)
                    for i in range(number_of_frames):
                        ret, frame = self.get_frame()
                        if ret:
                            file_name = 'frame-' + time.strftime('%d-%m-%Y-%H-%M-%S') + '-' + str(i) + '.jpg'
                            cv2.imwrite(SnapshotStorage.get_storage_dir() + file_name,
                                        cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                        time.sleep(self.__snapshot_frequency)
                    movement_finished = True
                except AttributeError:
                    pass

        self.__wait_for_start()
        self.__play_double_beep()

        self.__recording_thread = Thread(target=__process_recording, args=())
        self.__recording_thread.daemon = True
        self.__recording_thread.start()

        self.__wait_until_recording_stops()
        self.__play_double_beep()

    def __update(self) -> None:
        while True:
            if self.__video.isOpened():
                self.status, self.frame = self.__video.read()
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

    def __wait_until_recording_stops(self) -> None:
        while self.__recording_thread.is_alive():
            time.sleep(0.5)

    def __wait_for_start(self) -> None:
        for i in range(self.__delay):
            self.__play_beep()
            time.sleep(1)

    def __play_beep(self) -> None:
        sys.stdout.write('\a')
        sys.stdout.flush()

    def __play_double_beep(self) -> None:
        sys.stdout.write('\a')
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write('\a')
        sys.stdout.flush()
