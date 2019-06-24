from abc import abstractmethod


class PopupInterface:

    @abstractmethod
    def show(self) -> None:
        pass
