from app.filesystem.result_storage import ResultStorage


class ReportWriter:

    def __init__(self, result_storage: ResultStorage) -> None:
        self.__result_storage = result_storage

    def write_report(self, report: str) -> None:
        file = open(self.__result_storage.get_storage_dir() + 'result.txt', 'w')
        file.write(report)
        file.close()
