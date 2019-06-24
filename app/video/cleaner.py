from os import *
from app.filesystem.snapshot_storage import SnapshotStorage


class Cleaner:

    @staticmethod
    def clean_snapshot_storage() -> None:
        for file in listdir(SnapshotStorage.get_storage_dir()):
            if file.endswith('.jpg'):
                remove(SnapshotStorage.get_storage_dir() + file)
