import os
import time


class ResultStorage:

    def __init__(self) -> None:
        self.__process_timestamp = str(int(time.time()))

    def get_storage_dir(self) -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return current_dir + '/../../' + 'reports/' + self.__process_timestamp + '/'
