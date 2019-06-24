import os


class SnapshotStorage:

    @staticmethod
    def get_storage_dir() -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return current_dir + '/../../' + 'tmp/'
