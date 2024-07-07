from abc import ABC, abstractmethod
from pathlib import Path


class BaseFileReader(ABC):
    @abstractmethod
    def read_file(self, filename: Path) -> list[str]:
        pass


class FileReader(BaseFileReader):
    def __init__(self) -> None:
        super().__init__()

    def read_file(self, filename: Path) -> list[str]:
        with Path.open(filename, encoding="utf-8") as data_file:
            return data_file.readlines()


class DummyFileReader(BaseFileReader):
    def read_file(self, filename: Path) -> list[str]:
        _ = filename
        return ["dummy", "data"]
