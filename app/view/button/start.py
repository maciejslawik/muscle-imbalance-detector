from tkinter import *
from app.view.button.button_interface import ButtonInterface
from app.video.cleaner import Cleaner
from app.openpose.image_processor import ImageProcessor
from app.openpose.keypoint_data_transformer import KeypointDataTransformer
from app.openpose.report_generator import ReportGenerator
from app.filesystem.report_writer import ReportWriter
from app.view.popup.report import ReportPopup
from app.filesystem.result_storage import ResultStorage


class StartButton(ButtonInterface):

    def __init__(self, video_capture, time_input) -> None:
        self.__video_capture = video_capture
        self.__time_input = time_input
        self.__button = Button(None, text='Start', command=self.__start_measurements)
        result_storage = ResultStorage()
        self.__openpose_image_processor = ImageProcessor(result_storage)
        self.__report_writer = ReportWriter(result_storage)
        self.__cleaner = Cleaner()
        self.__keypoint_data_transformer = KeypointDataTransformer()
        self.__report_generator = ReportGenerator()

    def build(self) -> Button:
        return self.__button

    def __start_measurements(self) -> None:
        # movement_time = int(self.__time_input.input.get())
        # self.__video_capture.record(movement_time)
        image_data = self.__openpose_image_processor.process_images()
        self.__cleaner.clean_snapshot_storage()
        keypoints_data = self.__keypoint_data_transformer.get_keypoints_data(image_data)
        report = self.__report_generator.generate_report(keypoints_data)
        self.__report_writer.write_report(report)
        ReportPopup(report).show()
        self.__init_temporary_dependencies()

    def __init_temporary_dependencies(self) -> None:
        result_storage = ResultStorage()
        self.__openpose_image_processor = ImageProcessor(result_storage)
        self.__report_writer = ReportWriter(result_storage)
